from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

def get_produtor(db: Session, produtor_id: int):
    logger.info(f"Buscando produtor com ID: {produtor_id}")
    return db.query(models.Produtor).filter(models.Produtor.id == produtor_id).first()

def get_produtor_by_cpf_cnpj(db: Session, cpf_cnpj: str):
    logger.info(f"Buscando produtor por CPF/CNPJ: {cpf_cnpj}")
    return db.query(models.Produtor).filter(models.Produtor.cpf_cnpj == cpf_cnpj).first()

def get_produtores(db: Session, skip: int = 0, limit: int = 100):
    logger.info(f"Buscando produtores com skip: {skip}, limit: {limit}")
    return db.query(models.Produtor).offset(skip).limit(limit).all()

def create_produtor(db: Session, produtor: schemas.ProdutorCreate):
    logger.info(f"Criando novo produtor: {produtor.nome}")
    db_produtor = models.Produtor(
        cpf_cnpj=produtor.cpf_cnpj,
        nome=produtor.nome
    )
    db.add(db_produtor)
    db.commit()
    db.refresh(db_produtor)

    if produtor.fazendas:
        for fazenda_data in produtor.fazendas:
            db_fazenda = models.Fazenda(
                nome=fazenda_data.nome,
                cidade=fazenda_data.cidade,
                estado=fazenda_data.estado,
                area_total=fazenda_data.area_total,
                area_agricultavel=fazenda_data.area_agricultavel,
                area_vegetacao=fazenda_data.area_vegetacao,
                produtor_id=db_produtor.id
            )
            db.add(db_fazenda)
            db.commit()
            db.refresh(db_fazenda)

            if fazenda_data.culturas:
                for cultura_data in fazenda_data.culturas:
                    db_cultura = models.Cultura(
                        nome=cultura_data.nome,
                        safra=cultura_data.safra,
                        fazenda_id=db_fazenda.id
                    )
                    db.add(db_cultura)
                db.commit()
                db.refresh(db_fazenda)

    logger.info(f"Produtor criado com sucesso. ID: {db_produtor.id}")
    return db_produtor

def update_produtor(db: Session, produtor_id: int, produtor: schemas.ProdutorCreate):
    logger.info(f"Atualizando produtor com ID: {produtor_id}")
    db_produtor = get_produtor(db, produtor_id)
    if not db_produtor:
        return None

    # Atualiza nome
    db_produtor.nome = produtor.nome
    db.commit()
    db.refresh(db_produtor)

    # Sincroniza fazendas
    fazendas_payload = produtor.fazendas or []
    fazendas_ids_payload = [f.id for f in fazendas_payload if hasattr(f, 'id') and f.id]
    fazendas_db = {f.id: f for f in db_produtor.fazendas}

    # Remove fazendas que não estão mais no payload
    for fazenda in db_produtor.fazendas[:]:
        if fazenda.id not in fazendas_ids_payload:
            db.delete(fazenda)
    db.commit()

    # Atualiza ou cria fazendas
    for fazenda_data in fazendas_payload:
        if hasattr(fazenda_data, 'id') and fazenda_data.id in fazendas_db:
            # Atualiza fazenda existente
            fazenda = fazendas_db[fazenda_data.id]
            fazenda.nome = fazenda_data.nome
            fazenda.cidade = fazenda_data.cidade
            fazenda.estado = fazenda_data.estado
            fazenda.area_total = fazenda_data.area_total
            fazenda.area_agricultavel = fazenda_data.area_agricultavel
            fazenda.area_vegetacao = fazenda_data.area_vegetacao
            db.commit()
            db.refresh(fazenda)
        else:
            # Cria nova fazenda
            fazenda = models.Fazenda(
                nome=fazenda_data.nome,
                cidade=fazenda_data.cidade,
                estado=fazenda_data.estado,
                area_total=fazenda_data.area_total,
                area_agricultavel=fazenda_data.area_agricultavel,
                area_vegetacao=fazenda_data.area_vegetacao,
                produtor_id=db_produtor.id
            )
            db.add(fazenda)
            db.commit()
            db.refresh(fazenda)
        # Sincroniza culturas da fazenda
        culturas_payload = getattr(fazenda_data, 'culturas', [])
        culturas_ids_payload = [c.id for c in culturas_payload if hasattr(c, 'id') and c.id]
        culturas_db = {c.id: c for c in fazenda.culturas}
        # Remove culturas que não estão mais no payload
        for cultura in fazenda.culturas[:]:
            if cultura.id not in culturas_ids_payload:
                db.delete(cultura)
        db.commit()
        # Atualiza ou cria culturas
        for cultura_data in culturas_payload:
            if hasattr(cultura_data, 'id') and cultura_data.id in culturas_db:
                cultura = culturas_db[cultura_data.id]
                cultura.nome = cultura_data.nome
                cultura.safra = cultura_data.safra
                db.commit()
                db.refresh(cultura)
            else:
                cultura = models.Cultura(
                    nome=cultura_data.nome,
                    safra=cultura_data.safra,
                    fazenda_id=fazenda.id
                )
                db.add(cultura)
        db.commit()
        db.refresh(fazenda)

    db.refresh(db_produtor)
    logger.info(f"Produtor atualizado com sucesso. ID: {produtor_id}")
    return db_produtor

def delete_produtor(db: Session, produtor_id: int):
    logger.info(f"Deletando produtor com ID: {produtor_id}")
    db_produtor = get_produtor(db, produtor_id)
    if not db_produtor:
        return False
    
    db.delete(db_produtor)
    db.commit()
    logger.info(f"Produtor deletado com sucesso. ID: {produtor_id}")
    return True

def get_fazenda(db: Session, fazenda_id: int):
    logger.info(f"Buscando fazenda com ID: {fazenda_id}")
    return db.query(models.Fazenda).filter(models.Fazenda.id == fazenda_id).first()

def get_fazendas_by_produtor(db: Session, produtor_id: int):
    logger.info(f"Buscando fazendas do produtor ID: {produtor_id}")
    return db.query(models.Fazenda).filter(models.Fazenda.produtor_id == produtor_id).all()

def get_fazendas(db: Session, skip: int = 0, limit: int = 100):
    logger.info(f"Buscando fazendas com skip: {skip}, limit: {limit}")
    return db.query(models.Fazenda).offset(skip).limit(limit).all()

def create_fazenda(db: Session, fazenda: schemas.FazendaCreate, produtor_id: int):
    logger.info(f"Criando nova fazenda para produtor ID: {produtor_id}")
    db_fazenda = models.Fazenda(
        nome=fazenda.nome,
        cidade=fazenda.cidade,
        estado=fazenda.estado,
        area_total=fazenda.area_total,
        area_agricultavel=fazenda.area_agricultavel,
        area_vegetacao=fazenda.area_vegetacao,
        produtor_id=produtor_id
    )
    db.add(db_fazenda)
    db.commit()
    db.refresh(db_fazenda)
    
    if fazenda.culturas:
        for cultura_data in fazenda.culturas:
            db_cultura = models.Cultura(
                nome=cultura_data.nome,
                safra=cultura_data.safra,
                fazenda_id=db_fazenda.id
            )
            db.add(db_cultura)
        db.commit()
        db.refresh(db_fazenda)
    
    logger.info(f"Fazenda criada com sucesso. ID: {db_fazenda.id}")
    return db_fazenda

def update_fazenda(db: Session, fazenda_id: int, fazenda: schemas.FazendaUpdate):
    logger.info(f"Atualizando fazenda com ID: {fazenda_id}")
    db_fazenda = get_fazenda(db, fazenda_id)
    if not db_fazenda:
        return None
    
    update_data = fazenda.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_fazenda, field, value)
    
    db.commit()
    db.refresh(db_fazenda)
    logger.info(f"Fazenda atualizada com sucesso. ID: {fazenda_id}")
    return db_fazenda

def delete_fazenda(db: Session, fazenda_id: int):
    logger.info(f"Deletando fazenda com ID: {fazenda_id}")
    db_fazenda = get_fazenda(db, fazenda_id)
    if not db_fazenda:
        return False
    
    db.delete(db_fazenda)
    db.commit()
    logger.info(f"Fazenda deletada com sucesso. ID: {fazenda_id}")
    return True

def get_cultura(db: Session, cultura_id: int):
    logger.info(f"Buscando cultura com ID: {cultura_id}")
    return db.query(models.Cultura).filter(models.Cultura.id == cultura_id).first()

def get_culturas_by_fazenda(db: Session, fazenda_id: int):
    logger.info(f"Buscando culturas da fazenda ID: {fazenda_id}")
    return db.query(models.Cultura).filter(models.Cultura.fazenda_id == fazenda_id).all()

def create_cultura(db: Session, cultura: schemas.CulturaCreate, fazenda_id: int):
    logger.info(f"Criando nova cultura para fazenda ID: {fazenda_id}")
    db_cultura = models.Cultura(
        nome=cultura.nome,
        safra=cultura.safra,
        fazenda_id=fazenda_id
    )
    db.add(db_cultura)
    db.commit()
    db.refresh(db_cultura)
    logger.info(f"Cultura criada com sucesso. ID: {db_cultura.id}")
    return db_cultura

def delete_cultura(db: Session, cultura_id: int):
    logger.info(f"Deletando cultura com ID: {cultura_id}")
    db_cultura = get_cultura(db, cultura_id)
    if not db_cultura:
        return False
    
    db.delete(db_cultura)
    db.commit()
    logger.info(f"Cultura deletada com sucesso. ID: {cultura_id}")
    return True

def get_dashboard_stats(db: Session) -> Dict[str, Any]:
    logger.info("Gerando estatísticas do dashboard")
    
    total_fazendas = db.query(func.count(models.Fazenda.id)).scalar()
    
    total_hectares = db.query(func.sum(models.Fazenda.area_total)).scalar() or 0
    
    por_estado = db.query(
        models.Fazenda.estado,
        func.count(models.Fazenda.id).label('quantidade')
    ).group_by(models.Fazenda.estado).all()
    por_estado_dict = {estado: quantidade for estado, quantidade in por_estado}
    
    por_cultura = db.query(
        models.Cultura.nome,
        func.count(models.Cultura.id).label('quantidade')
    ).group_by(models.Cultura.nome).all()
    por_cultura_dict = {cultura: quantidade for cultura, quantidade in por_cultura}
    
    area_agricultavel = db.query(func.sum(models.Fazenda.area_agricultavel)).scalar() or 0
    area_vegetacao = db.query(func.sum(models.Fazenda.area_vegetacao)).scalar() or 0
    por_uso_solo = {
        "Área Agricultável": area_agricultavel,
        "Área de Vegetação": area_vegetacao
    }
    
    logger.info(f"Dashboard gerado - Fazendas: {total_fazendas}, Hectares: {total_hectares}")
    
    return {
        "total_fazendas": total_fazendas,
        "total_hectares": total_hectares,
        "por_estado": por_estado_dict,
        "por_cultura": por_cultura_dict,
        "por_uso_solo": por_uso_solo
    } 