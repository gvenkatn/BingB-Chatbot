from fastapi import FastAPI, Request, Depends, HTTPException
from database import SessionLocal, engine
from sentence_transformers import SentenceTransformer
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, schemas
import numpy as np

from sqlalchemy.sql import func

from database import SessionLocal, engine

model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize FastAPI App
app = FastAPI()

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# HTTP Basic Authentication
security = HTTPBasic()

# Dependency: Get Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_most_similar_question(user_query, faqs):
    """Find the most similar question using sentence embeddings."""
    user_embedding = model.encode(user_query)
    faq_embeddings = [model.encode(faq.question) for faq in faqs]
    
    # Compute cosine similarity
    similarities = [np.dot(user_embedding, faq_emb) / (np.linalg.norm(user_embedding) * np.linalg.norm(faq_emb)) for faq_emb in faq_embeddings]
    
    best_match_index = np.argmax(similarities)
    return faqs[best_match_index] if similarities[best_match_index] > 0.5 else None  # Only return if similarity is above 50%

@app.post("/webhook/")
async def dialogflow_webhook(request: Request, db: Session = Depends(get_db)):
    req = await request.json()
    intent_name = req.get('queryResult', {}).get('intent', {}).get('displayName')
    user_query = req.get('queryResult', {}).get('queryText')

    response_text = "I'm not sure about that. Can you try rephrasing?"

    if intent_name == "FAQs":
        faqs = db.query(models.FAQ).all()
        best_match = get_most_similar_question(user_query, faqs)
        if best_match:
            response_text = best_match.answer

    elif intent_name == "CourseInfo":
        courses = db.query(models.Course).all()
        best_match = get_most_similar_question(user_query, courses)
        if best_match:
            response_text = f"{best_match.course_name} ({best_match.course_code}): {best_match.description}"

    elif intent_name == "FacultyInfo":
        faculty = db.query(models.Faculty).all()
        best_match = get_most_similar_question(user_query, faculty)
        if best_match:
            response_text = f"Professor {best_match.name} ({best_match.email}) specializes in {best_match.research_interests}."

    return {"fulfillmentText": response_text}

# Authentication Dependency
def authenticate(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == credentials.username).first()
    if not user or not pwd_context.verify(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

# 🔑 Signup API
@app.post("/signup/")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

# 🔑 Login API
@app.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": "Login successful"}

# 📚 Public API: Get all FAQs (No Login Required)
@app.get("/faqs/", response_model=list[schemas.FAQResponse])
def get_faqs(db: Session = Depends(get_db)):
    return db.query(models.FAQ).all()

# 📌 Public API: Get all Courses (No Login Required)
@app.get("/courses/", response_model=list[schemas.CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()

# 👨‍🏫 Public API: Get all Faculty (No Login Required)
@app.get("/faculty/", response_model=list[schemas.FacultyResponse])
def get_faculty(db: Session = Depends(get_db)):
    return db.query(models.Faculty).all()

# 📚 Protected API: Add New FAQ (Login Required)
@app.post("/faqs/", response_model=schemas.FAQResponse)
def create_faq(faq: schemas.FAQCreate, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    new_faq = models.FAQ(**faq.dict())
    db.add(new_faq)
    db.commit()
    db.refresh(new_faq)
    return new_faq

# 📚 Protected API: Update an FAQ (Login Required)
@app.put("/faqs/{faq_id}/", response_model=schemas.FAQResponse)
def update_faq(faq_id: int, faq_update: schemas.FAQCreate, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    faq = db.query(models.FAQ).filter(models.FAQ.id == faq_id).first()
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")

    for key, value in faq_update.dict().items():
        setattr(faq, key, value)

    db.commit()
    db.refresh(faq)
    return faq

# 🗑️ Protected API: Delete an FAQ (Login Required)
@app.delete("/faqs/{faq_id}/", response_model=dict)
def delete_faq(faq_id: int, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    faq = db.query(models.FAQ).filter(models.FAQ.id == faq_id).first()
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")

    db.delete(faq)
    db.commit()
    return {"message": "FAQ deleted successfully"}

# 📌 Protected API: Add New Course (Login Required)
@app.post("/courses/", response_model=schemas.CourseResponse)
def create_course(course: schemas.CourseCreate, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    new_course = models.Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

# 📌 Protected API: Update a Course (Login Required)
@app.put("/courses/{course_id}/", response_model=schemas.CourseResponse)
def update_course(course_id: int, course_update: schemas.CourseCreate, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    for key, value in course_update.dict().items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)
    return course

# 🗑️ Protected API: Delete a Course (Login Required)
@app.delete("/courses/{course_id}/", response_model=dict)
def delete_course(course_id: int, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    db.delete(course)
    db.commit()
    return {"message": "Course deleted successfully"}

# 👨‍🏫 Protected API: Add New Faculty (Login Required)
@app.post("/faculty/", response_model=schemas.FacultyResponse)
def create_faculty(faculty: schemas.FacultyCreate, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    new_faculty = models.Faculty(**faculty.dict())
    db.add(new_faculty)
    db.commit()
    db.refresh(new_faculty)
    return new_faculty

# 👨‍🏫 Protected API: Update Faculty (Login Required)
@app.put("/faculty/{faculty_id}/", response_model=schemas.FacultyResponse)
def update_faculty(faculty_id: int, faculty_update: schemas.FacultyCreate, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    faculty = db.query(models.Faculty).filter(models.Faculty.id == faculty_id).first()
    if not faculty:
        raise HTTPException(status_code=404, detail="Faculty not found")

    for key, value in faculty_update.dict().items():
        setattr(faculty, key, value)

    db.commit()
    db.refresh(faculty)
    return faculty

# 🗑️ Protected API: Delete Faculty (Login Required)
@app.delete("/faculty/{faculty_id}/", response_model=dict)
def delete_faculty(faculty_id: int, user: models.User = Depends(authenticate), db: Session = Depends(get_db)):
    faculty = db.query(models.Faculty).filter(models.Faculty.id == faculty_id).first()
    if not faculty:
        raise HTTPException(status_code=404, detail="Faculty not found")

    db.delete(faculty)
    db.commit()
    return {"message": "Faculty deleted successfully"}

@app.get("/")
def read_root():
    return {"message": "BingB Chatbot is running!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT is not set
    uvicorn.run(app, host="0.0.0.0", port=port)
