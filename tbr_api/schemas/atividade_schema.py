from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AtividadeBase(BaseModel):
    nome: str
    dataDeCriacao: datetime
    dataDeEdicao: datetime | None
    id_user: int


class Atividade(AtividadeBase):
    id: int

    class Config:
        orm_mode = True


class AtividadeCreate(BaseModel):
    nome: str
    id_user: int


class AtividadePut(BaseModel):
    nome: str
    id_user: int


class AtividadePatch(BaseModel):
    nome: str | None


class AtividadeSearch(BaseModel):
    nome: str | None
    id_user: int | None
    order: str | None
