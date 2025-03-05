from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = "postgresql://postgres@localhost/bingb"


# Create Engine
engine = create_engine(DATABASE_URL)

# Create a Session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base Model
Base = declarative_base()


