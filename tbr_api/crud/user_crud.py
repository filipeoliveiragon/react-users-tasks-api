from fastapi import HTTPException
from sqlalchemy.orm import Session
from tbr_api.infra.models.atividade_model import AtividadesModel

from tbr_api.schemas.user_schema import User, UserCreate, UserPatch, UserPut, UserSimple
from ..infra.models.user_model import UserModel

from tbr_api.crud.atividade_crud import deletaAtividade

def listarUsuarios(db: Session) -> UserModel:
    return db.query(UserModel).all()

def criaUsuario(db: Session, user_create: UserCreate) -> UserModel:
    db_user = UserModel(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def listaUsuario(db: Session, id: int):
    db_user = db.query(UserModel).filter(UserModel.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    return db_user

def editaUsuarioPut(db: Session, id: int, userPut: UserPut):
    db_user = db.query(UserModel).filter(UserModel.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    
    for key, value in userPut.dict().items():
        setattr(db_user, key, value)
        
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

def editaUsuarioPatch(db: Session, id: int, userPatch: UserPatch):
    db_user = db.query(UserModel).filter(UserModel.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    
    patch_fields = userPatch.dict(exclude_unset=True)
    
    for key, value in patch_fields.items():
        setattr(db_user, key, value)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

def deletaUsuario(db: Session, id: int):
    db_user = db.query(UserModel).filter(UserModel.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    
    if db_user.atividades is not None:
        db_atividades = db.query(AtividadesModel).filter(AtividadesModel.id_user == id).all()
        for item in db_atividades:
            deletaAtividade(db, item.id)
    
    db.delete(db_user)
    db.commit()
    
    return {"message": "Usuário deletado!"}

def buscaUsuario(db: Session, nome: str):
    db_user = db.query(UserModel).filter(UserModel.nome.ilike(f'%{nome}%')).all()
    return db_user