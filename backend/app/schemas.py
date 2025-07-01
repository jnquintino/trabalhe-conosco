from pydantic import BaseModel, validator, root_validator
from typing import List, Optional
from datetime import datetime
import re

class CulturaBase(BaseModel):
    nome: str
    safra: str

class CulturaCreate(CulturaBase):
    pass

class Cultura(CulturaBase):
    id: int
    fazenda_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class FazendaBase(BaseModel):
    nome: str
    cidade: str
    estado: str
    area_total: float
    area_agricultavel: float
    area_vegetacao: float
    
    @validator('area_total', 'area_agricultavel', 'area_vegetacao')
    def validate_areas(cls, v):
        if v <= 0:
            raise ValueError('Área deve ser maior que zero')
        return v

    @root_validator(skip_on_failure=True)
    def validate_area_sum(cls, values):
        area_total = values.get('area_total')
        area_agricultavel = values.get('area_agricultavel')
        area_vegetacao = values.get('area_vegetacao')
        if area_total is not None and area_agricultavel is not None and area_vegetacao is not None:
            if area_agricultavel + area_vegetacao > area_total:
                raise ValueError('Soma das áreas agricultável e vegetação não pode ultrapassar a área total')
        return values

class FazendaCreate(FazendaBase):
    culturas: Optional[List[CulturaCreate]] = []

class FazendaUpdate(BaseModel):
    nome: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    area_total: Optional[float] = None
    area_agricultavel: Optional[float] = None
    area_vegetacao: Optional[float] = None

class Fazenda(FazendaBase):
    id: int
    produtor_id: int
    culturas: List[Cultura] = []
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class ProdutorBase(BaseModel):
    cpf_cnpj: str
    nome: str
    
    @validator('cpf_cnpj')
    def validate_cpf_cnpj(cls, v):
        v = re.sub(r'[^\d]', '', v)
        
        if len(v) == 11:  # CPF
            if not cls._validate_cpf(v):
                raise ValueError('CPF inválido')
        elif len(v) == 14:  # CNPJ
            if not cls._validate_cnpj(v):
                raise ValueError('CNPJ inválido')
        else:
            raise ValueError('CPF deve ter 11 dígitos ou CNPJ deve ter 14 dígitos')
        
        return v
    
    @staticmethod
    def _validate_cpf(cpf):
        if len(set(cpf)) == 1:
            return False
        
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto
        
        if int(cpf[9]) != digito1:
            return False
        
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto
        
        return int(cpf[10]) == digito2
    
    @staticmethod
    def _validate_cnpj(cnpj):
        if len(set(cnpj)) == 1:
            return False
        
        multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * multiplicadores[i] for i in range(12))
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto
        
        if int(cnpj[12]) != digito1:
            return False
        
        multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * multiplicadores[i] for i in range(13))
        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto
        
        return int(cnpj[13]) == digito2

class ProdutorCreate(ProdutorBase):
    fazendas: Optional[List[FazendaCreate]] = []

class ProdutorUpdate(BaseModel):
    nome: Optional[str] = None

class Produtor(ProdutorBase):
    id: int
    fazendas: List[Fazenda] = []
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class DashboardStats(BaseModel):
    total_fazendas: int
    total_hectares: float
    por_estado: dict
    por_cultura: dict
    por_uso_solo: dict 