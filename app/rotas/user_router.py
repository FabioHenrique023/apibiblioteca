from fastapi import APIRouter, HTTPException, status, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas.user_schema import RequestUser, Response, Resquest
from schemas.login_schema import LoginSchema, RequestLogin, ResquestL, ResponseLogin, TokenResponse
import controller.user_controller as user_controle
from controller.user_controller import pwd_cripto, JWTBearer, JWTRepo

router_user = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

@router_user.post('/CreateUser')
async def create(request:RequestUser, db:Session=Depends(get_db)):
    user_controle.create_user(db, user_create = request.parameter)
    return Response(code = 200, status = "Ok", mensagem = "Tipo usuário cadastrado com sucesso!").dict(exclude_none=True)


@router_user.post('/login')
async def login(login_data: LoginSchema, db: Session = Depends(get_db)):
    try:
        _user = user_controle.busca_by_name(db, login_data.username)
        
        if not pwd_cripto.verify(login_data.password, _user.password):
            raise HTTPException(status_code=400, detail="Senha inválida")

        token = JWTRepo.generate_token({"sub": _user.username})
        return ResponseLogin(
            code="200",
            status="OK",
            mensagem="Login bem-sucedido!",
            resultado=TokenResponse(access_token=token, token_type="Bearer")
        )
    except HTTPException as http_error:
        raise http_error 
    except Exception as error:
        error_message = str(error)
        print(error_message)
        raise HTTPException(status_code=500, detail="Erro interno do servidor")

@router_user.get("/listartodos", dependencies=[Depends(JWTBearer())])
async def get_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _user = user_controle.get_user(db, skip, limit)
    return Response(code = 200, status = "Ok", mensagem ="Busca completa", resultado = _user).dict(exclude_none=True)
