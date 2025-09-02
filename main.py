from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

import models,schemas
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='API Catálogo de Filmes')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return{'mensagem':'Bem-Vindo ao API de Filmes :)'}

@app.post('/filmes', response_model=schemas.Filme)
def criar_filme(filme:schemas.FilmeCreate,db:Session=Depends(get_db)):
    novo_filme = models.Filme(**filme.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme