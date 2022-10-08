from sqlalchemy import Column, Integer, String
from tbr_api.infra.config.database import Base
from sqlalchemy.orm import relationship

from tbr_api.infra.models import atividade_model

class UserModel(Base):
    __tablename__ = "tbl_users"

    id = Column(Integer, primary_key =True,autoincrement = True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable = False)
    telefone = Column(String, nullable = False)
    
    atividades = relationship("AtividadesModel")