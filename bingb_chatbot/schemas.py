from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FAQBase(BaseModel):
    question: str
    answer: str
    category: Optional[str] = None
    tags: Optional[str] = None
    priority_level: Optional[str] = "Medium"

class FAQCreate(FAQBase):
    pass

class FAQResponse(FAQBase):
    id: int
    last_updated: datetime

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 📚 Course Schema
class CourseBase(BaseModel):
    course_code: str
    course_name: str
    prerequisites: Optional[str] = None
    syllabus_link: Optional[str] = None
    credits: Optional[int] = None
    semester_offered: Optional[str] = None
    professor: Optional[str] = None
    classroom_location: Optional[str] = None
    mode_of_instruction: Optional[str] = None
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional

# 👨‍🏫 Faculty Schema
class FacultyBase(BaseModel):
    name: str
    email: str
    office_hours: Optional[str] = None
    department: Optional[str] = None
    phone_number: Optional[str] = None
    research_interests: Optional[str] = None
    office_location: Optional[str] = None
    website_link: Optional[str] = None

class FacultyCreate(FacultyBase):
    pass

class FacultyResponse(FacultyBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel

# User Signup Schema
class UserCreate(BaseModel):
    username: str
    password: str

# User Login Schema
class UserLogin(BaseModel):
    username: str
    password: str
