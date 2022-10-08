from typing import Optional
from fastapi import APIRouter, Depends
from tbr_api.dependencies import get_db
from sqlalchemy.orm import Session

from tbr_api.infra.models.atividade_model import AtividadesModel
from tbr_api.schemas.atividade_schema import Atividade, AtividadeCreate, AtividadePatch, AtividadePut, AtividadeSearch

from tbr_api.crud.atividade_crud import buscaAtividade, deletaAtividade, listaUsuarioAtividade, listarAtividades, criaAtividade, listaAtividade, editaAtividadePut

router = APIRouter(
    prefix="/atividade",
    tags=["Atividade"]
)

@router.get("/", response_model=list[Atividade])
async def getTasks(db: Session = Depends(get_db)):
    return listarAtividades(db)

@router.post("/", response_model=Atividade)
async def createTask(atividade_create: AtividadeCreate, db: Session = Depends(get_db)):
    return criaAtividade(db, atividade_create)

@router.get("/{id}", response_model=Atividade)
async def getTasID(id: int, db: Session = Depends(get_db)):
    return listaAtividade(db, id)

@router.put("/{id}", response_model=Atividade)
async def putTask(id: int, atividade_Put: AtividadePut, db: Session = Depends(get_db)):
    return editaAtividadePut(db, id, atividade_Put)

@router.patch("/{id}", response_model=Atividade)
async def putTask(id: int, atividade_patch: AtividadePatch, db: Session = Depends(get_db)):
    return editaAtividadePut(db, id, atividade_patch)

@router.delete("/{id}")
async def deleteTask(id: int, db: Session = Depends(get_db)):
    return deletaAtividade(db, id)

@router.get("/usertask/{id}")
async def getTaskUser(id: int, db: Session = Depends(get_db)):
    return listaUsuarioAtividade(db, id)

@router.get("/busca/", response_model=list[Atividade])
async def searchTask(nome: str | None = None, id_user: int | None = None, db: Session = Depends(get_db)):
    return buscaAtividade(db, nome, id_user)