import email
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
import datetime

from models.endereco_model import Endereco_model
from models.tipo_usuario_model import Tipo_usuario_model


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)

    first_name = Column(String)
    last_name = Column(String)
    
    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime)
    
    #Relação com a tabela endereço
    id_tabela_endereco = Column(Integer, ForeignKey(Endereco_model.id))
    endereco = relationship(Endereco_model, back_populates="users")
    
    #Relação com a tabela tipo usuário
    id_tabela_tipo_usuario = Column(Integer, ForeignKey(Tipo_usuario_model.id)) 
    tipo_usuario = relationship(Tipo_usuario_model, back_populates="users")