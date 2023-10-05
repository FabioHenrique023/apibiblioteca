from sqlalchemy.orm import Session
from models.tipo_usuario_model import Tipo_usuario_model 
from schemas.tipo_usuario_schema import Tipo_usuario_schemas 

#Função para obter uma lista de tipos de usuários com paginação
def get_tipousuario(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tipo_usuario_model).offset(skip).limit(limit).all()

#Função para obter um único tipo de usuário a partir do ID
def get_tipousuario_id(db: Session, id: int):
    resultado = db.query(Tipo_usuario_model).filter(Tipo_usuario_model.id == id).first()
    
    if resultado is None:
        return None
    
    return resultado

#Função para criar tipos de usuários
def create_tipousuario(db:Session, tipo_usuario_create = Tipo_usuario_schemas):
    _tipo_usuario = Tipo_usuario_model(nome = tipo_usuario_create.nome)
    db.add(_tipo_usuario)
    db.commit()
    db.refresh(_tipo_usuario)
    return _tipo_usuario

#Função para deletar um tipo de usuário a partir do ID
def delete_tipousuario(db:Session, id:int):
    _tipo_usuario = get_tipousuario_id(db=db, id=id)
    db.delete(_tipo_usuario)
    db.commit()
    
#Função para atualizar os dados do tipo de usuário
def update_tipousuario(db:Session, id=int, nome=str):
    _tipo_usuario = get_tipousuario_id(db=db, id=id)
    
    if _tipo_usuario is None:
        return None 
    
    _tipo_usuario.nome = nome 
    db.commit()
    db.refresh(_tipo_usuario)
    return _tipo_usuario