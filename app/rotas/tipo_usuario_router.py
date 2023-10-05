from fastapi import APIRouter, HTTPException, status, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas.tipo_usuario_schema import Response, RequestTipo, Tipo_usuario_schemas, Request
import controller.tipo_usuario_controller as tipousuario

router_tipo_usuario = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

@router_tipo_usuario.post('/CriarTipoUsuario')
async def create(request:RequestTipo, db:Session=Depends(get_db)):
    tipousuario.create_tipousuario(db, tipo_usuario_create = request.parameter)
    return Response(code = 200, status = "Ok", mensagem = "Tipo usuário cadastrado com sucesso!").dict(exclude_none=True)

@router_tipo_usuario.get("/listartodos")
async def get_tipo_usuario(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _tipo = tipousuario.get_tipousuario(db, skip, limit)
    return Response(code = 200, status = "Ok", mensagem ="Busca completa", resultado = _tipo).dict(exclude_none=True)
 
@router_tipo_usuario.get("/id/{id}")
async def get_by_id(id:int, db:Session = Depends(get_db)):
    _tipo_usuario = tipousuario.get_tipousuario_id(db, id)
    
    if _tipo_usuario:
        return Response(code = 200, status = "Ok", mensagem = f"Busca concluída com sucesso: {id}", resultado = _tipo_usuario)
    else:
        raise HTTPException(detail= "ID não existe", status_code = status.HTTP_404_NOT_FOUND)
    
@router_tipo_usuario.patch("/update")
async def update_tipo_usuario(request: RequestTipo, db:Session = Depends(get_db)):
    _tipo_usuario = tipousuario.update_tipousuario(db, id = request.parameter.id, nome = request.parameter.nome)
    
    if _tipo_usuario:
        return Response(code = 200, status="Ok", mensagem = "Alterado com sucesso!", resultado = _tipo_usuario)
    else:
        raise HTTPException(detail="ID não encontrado", status_code = status.HTTP_404_NOT_FOUND)
    
@router_tipo_usuario.delete("/delete/{id}")
async def delete_tipo(id: int, db: Session = Depends(get_db)):
    _tipo_usuario = tipousuario.get_tipousuario_id(db, id)
    
    if _tipo_usuario:
        tipousuario.delete_tipousuario(db, id=id)
        return Response(code =  200, status = "Ok", mensagem = "Deletado com sucesso!")
    
    elif _tipo_usuario is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Tipo de usuário não encontrado")
    
    else:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "Tente novamente")