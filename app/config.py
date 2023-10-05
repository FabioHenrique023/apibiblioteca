from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/apibiblioteca"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Configuração do JWT
SECRET_KEY="Tay@code19"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 30