from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import logging
from . import crud, schemas, database

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/produtores/", response_model=schemas.Produtor, status_code=status.HTTP_201_CREATED)
def create_produtor(produtor: schemas.ProdutorCreate, db: Session = Depends(database.get_db)):
    """Criar um novo produtor rural"""
    logger.info(f"Recebida requisição para criar produtor: {produtor.nome}")
    
    db_produtor = crud.get_produtor_by_cpf_cnpj(db, cpf_cnpj=produtor.cpf_cnpj)
    if db_produtor:
        logger.warning(f"Tentativa de criar produtor com CPF/CNPJ já existente: {produtor.cpf_cnpj}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF/CNPJ já cadastrado"
        )
    
    return crud.create_produtor(db=db, produtor=produtor)

@router.get("/produtores/", response_model=List[schemas.Produtor])
def read_produtores(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """Listar todos os produtores rurais"""
    logger.info(f"Recebida requisição para listar produtores - skip: {skip}, limit: {limit}")
    produtores = crud.get_produtores(db, skip=skip, limit=limit)
    return produtores

@router.get("/produtores/{produtor_id}", response_model=schemas.Produtor)
def read_produtor(produtor_id: int, db: Session = Depends(database.get_db)):
    """Buscar um produtor específico por ID"""
    logger.info(f"Recebida requisição para buscar produtor ID: {produtor_id}")
    db_produtor = crud.get_produtor(db, produtor_id=produtor_id)
    if db_produtor is None:
        logger.warning(f"Produtor não encontrado. ID: {produtor_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produtor não encontrado"
        )
    return db_produtor

@router.put("/produtores/{produtor_id}", response_model=schemas.Produtor)
def update_produtor(produtor_id: int, produtor: schemas.ProdutorCreate, db: Session = Depends(database.get_db)):
    """Atualizar um produtor existente"""
    logger.info(f"Recebida requisição para atualizar produtor ID: {produtor_id}")
    db_produtor = crud.update_produtor(db, produtor_id=produtor_id, produtor=produtor)
    if db_produtor is None:
        logger.warning(f"Produtor não encontrado para atualização. ID: {produtor_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produtor não encontrado"
        )
    return db_produtor

@router.delete("/produtores/{produtor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_produtor(produtor_id: int, db: Session = Depends(database.get_db)):
    """Deletar um produtor"""
    logger.info(f"Recebida requisição para deletar produtor ID: {produtor_id}")
    success = crud.delete_produtor(db, produtor_id=produtor_id)
    if not success:
        logger.warning(f"Produtor não encontrado para deleção. ID: {produtor_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produtor não encontrado"
        )

@router.post("/produtores/{produtor_id}/fazendas/", response_model=schemas.Fazenda, status_code=status.HTTP_201_CREATED)
def create_fazenda(produtor_id: int, fazenda: schemas.FazendaCreate, db: Session = Depends(database.get_db)):
    """Criar uma nova fazenda para um produtor"""
    logger.info(f"Recebida requisição para criar fazenda para produtor ID: {produtor_id}")
    
    db_produtor = crud.get_produtor(db, produtor_id=produtor_id)
    if not db_produtor:
        logger.warning(f"Produtor não encontrado para criar fazenda. ID: {produtor_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produtor não encontrado"
        )
    
    return crud.create_fazenda(db=db, fazenda=fazenda, produtor_id=produtor_id)

@router.get("/produtores/{produtor_id}/fazendas/", response_model=List[schemas.Fazenda])
def read_fazendas_by_produtor(produtor_id: int, db: Session = Depends(database.get_db)):
    """Listar todas as fazendas de um produtor"""
    logger.info(f"Recebida requisição para listar fazendas do produtor ID: {produtor_id}")
    
    db_produtor = crud.get_produtor(db, produtor_id=produtor_id)
    if not db_produtor:
        logger.warning(f"Produtor não encontrado. ID: {produtor_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produtor não encontrado"
        )
    
    fazendas = crud.get_fazendas_by_produtor(db, produtor_id=produtor_id)
    return fazendas

@router.get("/fazendas/", response_model=List[schemas.Fazenda])
def read_fazendas(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """Listar todas as fazendas"""
    logger.info(f"Recebida requisição para listar fazendas - skip: {skip}, limit: {limit}")
    fazendas = crud.get_fazendas(db, skip=skip, limit=limit)
    return fazendas

@router.get("/fazendas/{fazenda_id}", response_model=schemas.Fazenda)
def read_fazenda(fazenda_id: int, db: Session = Depends(database.get_db)):
    """Buscar uma fazenda específica por ID"""
    logger.info(f"Recebida requisição para buscar fazenda ID: {fazenda_id}")
    db_fazenda = crud.get_fazenda(db, fazenda_id=fazenda_id)
    if db_fazenda is None:
        logger.warning(f"Fazenda não encontrada. ID: {fazenda_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fazenda não encontrada"
        )
    return db_fazenda

@router.put("/fazendas/{fazenda_id}", response_model=schemas.Fazenda)
def update_fazenda(fazenda_id: int, fazenda: schemas.FazendaUpdate, db: Session = Depends(database.get_db)):
    """Atualizar uma fazenda existente"""
    logger.info(f"Recebida requisição para atualizar fazenda ID: {fazenda_id}")
    db_fazenda = crud.update_fazenda(db, fazenda_id=fazenda_id, fazenda=fazenda)
    if db_fazenda is None:
        logger.warning(f"Fazenda não encontrada para atualização. ID: {fazenda_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fazenda não encontrada"
        )
    return db_fazenda

@router.delete("/fazendas/{fazenda_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fazenda(fazenda_id: int, db: Session = Depends(database.get_db)):
    """Deletar uma fazenda"""
    logger.info(f"Recebida requisição para deletar fazenda ID: {fazenda_id}")
    success = crud.delete_fazenda(db, fazenda_id=fazenda_id)
    if not success:
        logger.warning(f"Fazenda não encontrada para deleção. ID: {fazenda_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fazenda não encontrada"
        )

# Culturas
@router.post("/fazendas/{fazenda_id}/culturas/", response_model=schemas.Cultura, status_code=status.HTTP_201_CREATED)
def create_cultura(fazenda_id: int, cultura: schemas.CulturaCreate, db: Session = Depends(database.get_db)):
    """Criar uma nova cultura para uma fazenda"""
    logger.info(f"Recebida requisição para criar cultura para fazenda ID: {fazenda_id}")
    
    db_fazenda = crud.get_fazenda(db, fazenda_id=fazenda_id)
    if not db_fazenda:
        logger.warning(f"Fazenda não encontrada para criar cultura. ID: {fazenda_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fazenda não encontrada"
        )
    
    return crud.create_cultura(db=db, cultura=cultura, fazenda_id=fazenda_id)

@router.get("/fazendas/{fazenda_id}/culturas/", response_model=List[schemas.Cultura])
def read_culturas_by_fazenda(fazenda_id: int, db: Session = Depends(database.get_db)):
    """Listar todas as culturas de uma fazenda"""
    logger.info(f"Recebida requisição para listar culturas da fazenda ID: {fazenda_id}")
    
    db_fazenda = crud.get_fazenda(db, fazenda_id=fazenda_id)
    if not db_fazenda:
        logger.warning(f"Fazenda não encontrada. ID: {fazenda_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fazenda não encontrada"
        )
    
    culturas = crud.get_culturas_by_fazenda(db, fazenda_id=fazenda_id)
    return culturas

@router.delete("/culturas/{cultura_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cultura(cultura_id: int, db: Session = Depends(database.get_db)):
    """Deletar uma cultura"""
    logger.info(f"Recebida requisição para deletar cultura ID: {cultura_id}")
    success = crud.delete_cultura(db, cultura_id=cultura_id)
    if not success:
        logger.warning(f"Cultura não encontrada para deleção. ID: {cultura_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cultura não encontrada"
        )

@router.get("/dashboard/", response_model=schemas.DashboardStats)
def get_dashboard_stats(db: Session = Depends(database.get_db)):
    """Obter estatísticas do dashboard"""
    logger.info("Recebida requisição para obter estatísticas do dashboard")
    return crud.get_dashboard_stats(db) 