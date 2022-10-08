from pydantic import BaseModel
from ..schemas.atividade_schema import Atividade

class UserBase(BaseModel):
    nome: str
    email: str
    telefone: str
    atividades: list[Atividade]
    
class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    nome: str
    email: str
    telefone: str
    
class UserPatch(BaseModel):
    nome: str | None
    email: str | None
    telefone: str | None
    
class UserPut(UserPatch):
    pass

class UserSimple(BaseModel):
    nome: str
    email: str
    telefone: str
    
class UserSearch(BaseModel):
    nome: str