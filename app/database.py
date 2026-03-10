
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv 
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}"

engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}"))
    conn.commit()

#conexão com o banco de dados ja criado
DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"

#criar um "motor" que fara o gerenciamento da conexão
engine = create_engine(DATABASE_URL)

#criando uma seção pra executar os comandos SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#cria um objeto da base de dados manipulavel pelo Python
Base = declarative_base()

# injeção de dependencia: injeta a sessão do bando de dados
#em cada rota que for criada
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()