from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format( 
    os.getenv('DB_HOST_USERNAME'),
    os.getenv('DB_HOST_PASSWORD'),
    os.getenv('DB_HOST_HOSTNAME'),
    os.getenv('DB_HOST_PORT'),
    os.getenv('DB_HOST_DATABASE') 
)

engine = create_engine( SQLALCHEMY_DATABASE_URL )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()