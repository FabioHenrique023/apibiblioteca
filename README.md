<h1 align="center">APIBIBLIOTECA</h1>

A Biblioteca API tem como objetivo gerenciar o processo interno de uma biblioteca, incluindo funcionalidades para o empréstimo de livros e outras operações relacionadas ao gerenciamento da biblioteca. Atualmente, o projeto está focado no desenvolvimento do back-end da aplicação por meio desta API, com planos futuros para implementar a interface de usuário.

## Tecnologias Utilizadas

- <img src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" width="16" height="16"> [FastAPI](https://fastapi.tiangolo.com/): Framework web para desenvolvimento rápido de APIs.
- <img src="https://cdn.icon-icons.com/icons2/112/PNG/512/python_18894.png" width="16" height="16"> [Python](https://www.python.org/): Linguagem de programação.
- <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg" width="16" height="16"> [PostgreSQL](https://www.postgresql.org/): Banco de dados relacional.
- <img src="https://atitudereflexiva.files.wordpress.com/2021/11/jwt_icon.png" width="16" height="16"> [JWT Authentication](https://jwt.io/): Autenticação baseada em tokens JWT.
- <img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_vscode_icon_130084.png" width="16" height="16"> [Visual Studio Code (VSCode)](https://code.visualstudio.com/): IDE de desenvolvimento.
- <img src="https://seeklogo.com/images/I/insomnia-logo-A35E09EB19-seeklogo.com.pngg" width="16" height="16"> [Insomnia](https://insomnia.rest/): Cliente HTTP para testar a API.

## Funcionalidades Atuais

- CRUD de Endereços.
- CRUD de tipos de usuários.
- CRUD de usuários
- Autenticação com JWT

## Instruções de Uso

1. **Instalação**:
   - Clone este repositório: `git clone https://github.com/FabioHenrique023/apibiblioteca.git`
   - Instale as dependências: `pip install -r requirements.txt`

2. **Configuração do Banco de Dados**:
   - Configure as informações do banco de dados no arquivo `config.py`.

3. **Executando a API**:
   - Execute o aplicativo FastAPI: `uvicorn main:app --host 0.0.0.0 --port 8000`

4. **Documentação da API**:
   - Acesse a documentação da API em `http://localhost:8000/docs` para testar as rotas e entender os endpoints disponíveis.

5. **Testando a Autenticação**:
   - Utilize o Insomnia para enviar solicitações autenticadas. Configure as solicitações com cabeçalhos JWT válidos.

6. **Contribuição**:
   - Siga as diretrizes de contribuição, se desejar contribuir para o projeto. Pull requests são bem-vindos!

7. **Licença**:
   - Este projeto está licenciado sob a <img src="license-icon.png" width="16" height="16"> [Sua Licença](LICENSE).

## Autor

Fábio Henrique Santos Moraes

<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>