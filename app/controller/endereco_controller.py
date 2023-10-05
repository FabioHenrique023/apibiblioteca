from sqlalchemy.orm import Session
from models.endereco_model import Endereco_model
from schemas.endereco_schema import Endereco_schema

def get_endereco(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Endereco_model).offset(skip).limit(limit).all()

def get_endereco_id(db: Session, id: int):
    resultado = db.query(Endereco_model).filter(Endereco_model.id == id).first()
    
    if resultado is None:
        return None
    
    return resultado

def create_endereco(db:Session, tipo_endereco_create = Endereco_schema):
    _endereco = Endereco_model(
                rua = tipo_endereco_create.rua, 
                bairro = tipo_endereco_create.bairro, 
                cep = tipo_endereco_create.cep
            )
    db.add(_endereco)
    db.commit()
    db.refresh(_endereco)
    return _endereco

def delete_endereco(db:Session, id:int):
    _endereco = get_endereco_id(db=db, id=id)
    db.delete(_endereco)
    db.commit()
    
def update_endereco(db:Session, id=int, rua = str, bairro = str, cep = int):
    _endereco = get_endereco_id(db=db, id=id)
    
    if _endereco is None:
        return None 
    
    _endereco.rua = rua
    _endereco.bairro = bairro
    _endereco.cep = cep
    db.commit()
    db.refresh(_endereco)
    return _endereco