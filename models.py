from sqlalchemy import Column, Integer, String, Float
from database import Base

class Filme(Base):
    __tablename__ = 'filmes'

    id_filme = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255), index=True)
    genero = Column(String(100), index=True)
    ano = Column(Integer)
    nota = Column(Float)
    