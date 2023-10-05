from fastapi import APIRouter, HTTPException, status, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas.endereco_schema import Response, RequestEndereco, Endereco_schema, Request
import controller.endereco_controller as endereco

router_endereco = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

@router_endereco.post('/CriarEndereco')
async def create(request:RequestEndereco, db:Session=Depends(get_db)):
    endereco.create_endereco(db, tipo_endereco_create = request.parameter)
    return Response(code = 200, status = "Ok", mensagem = "Endereço cadastrado com sucesso!").dict(exclude_none=True)


@router_endereco.get("/listartodos")
async def get_endereco(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _endereco = endereco.get_endereco(db, skip, limit)
    return Response(code = 200, status = "Ok", mensagem ="Busca completa", resultado = _endereco).dict(exclude_none=True)
 
@router_endereco.get("/id/{id}")
async def get_by_id(id:int, db:Session = Depends(get_db)):
    _endereco = endereco.get_endereco_id(db, id)
    
    if _endereco:
        return Response(code = 200, status = "Ok", mensagem = f"Busca concluída com sucesso: {id}", resultado = _endereco)
    else:
        raise HTTPException(detail= "ID não existe", status_code = status.HTTP_404_NOT_FOUND)
    
@router_endereco.patch("/update")
async def update_endereco(request: RequestEndereco, db:Session = Depends(get_db)):
    _endereco = endereco.update_endereco(db, id = request.parameter.id, rua = request.parameter.rua, 
                                             bairro = request.parameter.bairro, cep = request.parameter.cep)
    
    if _endereco:
        return Response(code = 200, status="Ok", mensagem = "Alterado com sucesso!", resultado = _endereco)
    else:
        raise HTTPException(detail="ID não encontrado", status_code = status.HTTP_404_NOT_FOUND)
    
@router_endereco.delete("/delete/{id}")
async def delete_tipo(id: int, db: Session = Depends(get_db)):
    _endereco = endereco.get_endereco_id(db, id)
    
    if _endereco:
        endereco.delete_endereco(db, id=id)
        return Response(code =  200, status = "Ok", mensagem = "Deletado com sucesso!")
    
    elif _endereco is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Tipo de usuário não encontrado")
    
    else:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "Tente novamente")