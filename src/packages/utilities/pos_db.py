from fastapi.params import Depends
from sqlalchemy.sql.annotation import Annotated
from sqlmodel import create_engine, SQLModel, Session
from src.configuration.configuration import settings


engine = create_engine(str(settings.sql_database_url), future=True, pool_pre_ping=True)

def create_db_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def close_session():
    engine.dispose()

def drop_database():
    SQLModel.metadata.drop_all(engine)
    create_db_tables()


SessionDep = Annotated[Session, Depends(get_session)]