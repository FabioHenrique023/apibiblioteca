from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config import Base

class Tipo_usuario_model(Base):
    __tablename__ = "tipousuario"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(30))
    
    users = relationship("Users", back_populates="tipo_usuario")