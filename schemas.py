from pydantic import BaseModel

class FilmeBase(BaseModel):

    titulo:str
    genero:str
    ano:int
    nota:float

class FilmeCreate(FilmeBase):
    pass

class Filme(FilmeBase):
    id_filme:int

    class Config:
        orm_mode = True