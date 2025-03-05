from sqlalchemy import Column, Integer, String, Text, DateTime, func
from database import Base

# FAQ Model
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.expression import func
from database import Base

class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, unique=True, nullable=False)
    answer = Column(Text, nullable=False)
    search_vector = Column(Text)  # Full-text search support

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String, unique=True, nullable=False)
    course_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    search_vector = Column(Text)

class Faculty(Base):
    __tablename__ = "faculty"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    email = Column(String, unique=True, nullable=False)
    research_interests = Column(Text, nullable=True)
    department = Column(String, nullable=True)
    search_vector = Column(Text)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

