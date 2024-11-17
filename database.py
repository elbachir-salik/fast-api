from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



URL_Database = 'postgresql://salik:1234@localhost:5432/QuizApp'

engine = create_engine(URL_Database)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()