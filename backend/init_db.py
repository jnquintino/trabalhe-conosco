#!/usr/bin/env python3
"""
Script de inicialização do banco de dados
Insere dados mockados para garantir que a aplicação sempre tenha dados para trabalhar
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Produtor, Fazenda, Cultura
from datetime import datetime
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    """Inicializa o banco de dados com dados mockados"""
    logger.info("Iniciando criação das tabelas...")
    
    # Criar todas as tabelas
    Base.metadata.create_all(bind=engine)
    
    # Verificar se já existem dados
    db = SessionLocal()
    try:
        existing_produtores = db.query(Produtor).count()
        if existing_produtores > 0:
            logger.info(f"Banco já possui {existing_produtores} produtores. Pulando inserção de dados mockados.")
            return
        
        logger.info("Inserindo dados mockados...")
        
        # Produtor 1 - João Silva
        produtor1 = Produtor(
            cpf_cnpj="12345678909",  # CPF válido
            nome="João Silva",
            created_at=datetime.utcnow()
        )
        db.add(produtor1)
        db.commit()
        db.refresh(produtor1)
        
        # Fazenda 1 do João
        fazenda1 = Fazenda(
            nome="Fazenda Santa Maria",
            cidade="São Paulo",
            estado="SP",
            area_total=1500.0,
            area_agricultavel=1200.0,
            area_vegetacao=300.0,
            produtor_id=produtor1.id,
            created_at=datetime.utcnow()
        )
        db.add(fazenda1)
        db.commit()
        db.refresh(fazenda1)
        
        # Culturas da Fazenda 1
        culturas_fazenda1 = [
            Cultura(nome="Soja", safra="2023", fazenda_id=fazenda1.id, created_at=datetime.utcnow()),
            Cultura(nome="Milho", safra="2023", fazenda_id=fazenda1.id, created_at=datetime.utcnow()),
            Cultura(nome="Feijão", safra="2023", fazenda_id=fazenda1.id, created_at=datetime.utcnow())
        ]
        for cultura in culturas_fazenda1:
            db.add(cultura)
        
        # Fazenda 2 do João
        fazenda2 = Fazenda(
            nome="Fazenda Boa Vista",
            cidade="Campinas",
            estado="SP",
            area_total=800.0,
            area_agricultavel=600.0,
            area_vegetacao=200.0,
            produtor_id=produtor1.id,
            created_at=datetime.utcnow()
        )
        db.add(fazenda2)
        db.commit()
        db.refresh(fazenda2)
        
        # Culturas da Fazenda 2
        culturas_fazenda2 = [
            Cultura(nome="Café", safra="2023", fazenda_id=fazenda2.id, created_at=datetime.utcnow()),
            Cultura(nome="Laranja", safra="2023", fazenda_id=fazenda2.id, created_at=datetime.utcnow())
        ]
        for cultura in culturas_fazenda2:
            db.add(cultura)
        
        # Produtor 2 - Maria Santos
        produtor2 = Produtor(
            cpf_cnpj="98765432100",  # CPF válido
            nome="Maria Santos",
            created_at=datetime.utcnow()
        )
        db.add(produtor2)
        db.commit()
        db.refresh(produtor2)
        
        # Fazenda da Maria
        fazenda3 = Fazenda(
            nome="Fazenda São João",
            cidade="Ribeirão Preto",
            estado="SP",
            area_total=2000.0,
            area_agricultavel=1600.0,
            area_vegetacao=400.0,
            produtor_id=produtor2.id,
            created_at=datetime.utcnow()
        )
        db.add(fazenda3)
        db.commit()
        db.refresh(fazenda3)
        
        # Culturas da Fazenda da Maria
        culturas_fazenda3 = [
            Cultura(nome="Cana-de-açúcar", safra="2023", fazenda_id=fazenda3.id, created_at=datetime.utcnow()),
            Cultura(nome="Soja", safra="2023", fazenda_id=fazenda3.id, created_at=datetime.utcnow()),
            Cultura(nome="Milho", safra="2023", fazenda_id=fazenda3.id, created_at=datetime.utcnow())
        ]
        for cultura in culturas_fazenda3:
            db.add(cultura)
        
        # Produtor 3 - Pedro Oliveira (CNPJ)
        produtor3 = Produtor(
            cpf_cnpj="11222333000181",  # CNPJ válido
            nome="Pedro Oliveira",
            created_at=datetime.utcnow()
        )
        db.add(produtor3)
        db.commit()
        db.refresh(produtor3)
        
        # Fazenda do Pedro
        fazenda4 = Fazenda(
            nome="Fazenda Grande",
            cidade="Uberlândia",
            estado="MG",
            area_total=3000.0,
            area_agricultavel=2400.0,
            area_vegetacao=600.0,
            produtor_id=produtor3.id,
            created_at=datetime.utcnow()
        )
        db.add(fazenda4)
        db.commit()
        db.refresh(fazenda4)
        
        # Culturas da Fazenda do Pedro
        culturas_fazenda4 = [
            Cultura(nome="Soja", safra="2023", fazenda_id=fazenda4.id, created_at=datetime.utcnow()),
            Cultura(nome="Milho", safra="2023", fazenda_id=fazenda4.id, created_at=datetime.utcnow()),
            Cultura(nome="Algodão", safra="2023", fazenda_id=fazenda4.id, created_at=datetime.utcnow()),
            Cultura(nome="Trigo", safra="2023", fazenda_id=fazenda4.id, created_at=datetime.utcnow())
        ]
        for cultura in culturas_fazenda4:
            db.add(cultura)
        
        # Produtor 4 - Ana Costa
        produtor4 = Produtor(
            cpf_cnpj="11144477735",  # CPF válido
            nome="Ana Costa",
            created_at=datetime.utcnow()
        )
        db.add(produtor4)
        db.commit()
        db.refresh(produtor4)
        
        # Fazenda da Ana
        fazenda5 = Fazenda(
            nome="Fazenda Vista Alegre",
            cidade="Goiânia",
            estado="GO",
            area_total=1200.0,
            area_agricultavel=900.0,
            area_vegetacao=300.0,
            produtor_id=produtor4.id,
            created_at=datetime.utcnow()
        )
        db.add(fazenda5)
        db.commit()
        db.refresh(fazenda5)
        
        # Culturas da Fazenda da Ana
        culturas_fazenda5 = [
            Cultura(nome="Arroz", safra="2023", fazenda_id=fazenda5.id, created_at=datetime.utcnow()),
            Cultura(nome="Feijão", safra="2023", fazenda_id=fazenda5.id, created_at=datetime.utcnow()),
            Cultura(nome="Soja", safra="2023", fazenda_id=fazenda5.id, created_at=datetime.utcnow())
        ]
        for cultura in culturas_fazenda5:
            db.add(cultura)
        
        # Commit final
        db.commit()
        
        logger.info("Dados mockados inseridos com sucesso!")
        logger.info(f"Total de produtores criados: 4")
        logger.info(f"Total de fazendas criadas: 5")
        logger.info(f"Total de culturas criadas: 15")
        
    except Exception as e:
        logger.error(f"Erro ao inserir dados mockados: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    logger.info("Iniciando script de inicialização do banco de dados...")
    init_db()
    logger.info("Script de inicialização concluído!") 