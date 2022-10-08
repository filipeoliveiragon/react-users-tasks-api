from fastapi import APIRouter, Depends
from tbr_api.dependencies import get_db
from sqlalchemy.orm import Session
from tbr_api.infra.models.user_model import UserModel

from tbr_api.schemas.user_schema import User, UserCreate, UserPatch, UserPut, UserSearch
from tbr_api.crud.user_crud import buscaUsuario, criaUsuario, listarUsuarios, listaUsuario, editaUsuarioPut, editaUsuarioPatch, deletaUsuario

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/", response_model=list[User])
async def getUsers(db: Session = Depends(get_db)):
    return listarUsuarios(db)


@router.get("/busca/{nome}", response_model=list[User])
async def searchUser(nome: str, db: Session = Depends(get_db)):
    return buscaUsuario(db, nome)


@router.post("/", response_model=User)
async def createUser(user_create: UserCreate, db: Session = Depends(get_db)):
    return criaUsuario(db, user_create)


@router.get("/{id}", response_model=User)
async def getUser(id: int, db: Session = Depends(get_db)):
    return listaUsuario(db, id)

@router.put("/{id}", response_model=User)
async def putUser(id: int, userPut: UserPut, db:Session = Depends(get_db)):
    return editaUsuarioPut(db, id, userPut)

@router.patch("/{id}", response_model=User)
async def patchUser(id:int, userPatch: UserPatch, db:Session = Depends(get_db)):
    return editaUsuarioPatch(db, id, userPatch)

@router.delete("/{id}")
async def deleteUser(id: int, db: Session = Depends(get_db)):
    return deletaUsuario(db, id)