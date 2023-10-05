from fastapi import FastAPI

from models.tipo_usuario_model import Base
from models.endereco_model import Base
from models.user_model import Base

from rotas.user_router import router_user
from rotas.tipo_usuario_router import router_tipo_usuario
from rotas.endereco_router import router_endereco

from config import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API: Biblioteca",
    version='0.0.1',
    description="Api desenvolvida na disciplina de Programação Orientado a Objetos II"
)

app.include_router(router_tipo_usuario, prefix="/tipouser", tags=["Tipo Usuário"])
app.include_router(router_endereco, prefix="/endereco", tags=["Endereço"])
app.include_router(router_user, prefix="/user", tags=["Users"])