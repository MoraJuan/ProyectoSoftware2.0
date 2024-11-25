from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///database.db', echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)