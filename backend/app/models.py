from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Produtor(Base):
    __tablename__ = "produtores"
    
    id = Column(Integer, primary_key=True, index=True)
    cpf_cnpj = Column(String, unique=True, index=True, nullable=False)
    nome = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    fazendas = relationship("Fazenda", back_populates="produtor", cascade="all, delete-orphan")

class Fazenda(Base):
    __tablename__ = "fazendas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    area_total = Column(Float, nullable=False)
    area_agricultavel = Column(Float, nullable=False)
    area_vegetacao = Column(Float, nullable=False)
    produtor_id = Column(Integer, ForeignKey("produtores.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    produtor = relationship("Produtor", back_populates="fazendas")
    culturas = relationship("Cultura", back_populates="fazenda", cascade="all, delete-orphan")

class Cultura(Base):
    __tablename__ = "culturas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    safra = Column(String, nullable=False)
    fazenda_id = Column(Integer, ForeignKey("fazendas.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    fazenda = relationship("Fazenda", back_populates="culturas") 