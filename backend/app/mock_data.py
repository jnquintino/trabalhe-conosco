from .models import Produtor, Fazenda, Cultura
from .database import SessionLocal
import logging

logger = logging.getLogger(__name__)

def create_mock_data():
    """Criar dados de exemplo para demonstração"""
    db = SessionLocal()
    try:
        if db.query(Produtor).count() > 0:
            logger.info("Dados já existem, pulando criação de mock data")
            return

        logger.info("Criando dados de exemplo...")

        produtor1 = Produtor(
            cpf_cnpj="12345678909",
            nome="João Silva Santos"
        )
        db.add(produtor1)
        db.flush()

        fazenda1 = Fazenda(
            nome="Fazenda Santa Maria",
            cidade="Ribeirão Preto",
            estado="SP",
            area_total=1500.0,
            area_agricultavel=1200.0,
            area_vegetacao=300.0,
            produtor_id=produtor1.id
        )
        db.add(fazenda1)
        db.flush()

        cultura1 = Cultura(
            nome="Soja",
            safra="2023",
            fazenda_id=fazenda1.id
        )
        cultura2 = Cultura(
            nome="Milho",
            safra="2023",
            fazenda_id=fazenda1.id
        )
        db.add_all([cultura1, cultura2])

        fazenda2 = Fazenda(
            nome="Fazenda Boa Vista",
            cidade="Uberlândia",
            estado="MG",
            area_total=800.0,
            area_agricultavel=600.0,
            area_vegetacao=200.0,
            produtor_id=produtor1.id
        )
        db.add(fazenda2)
        db.flush()

        cultura3 = Cultura(
            nome="Café",
            safra="2023",
            fazenda_id=fazenda2.id
        )
        db.add(cultura3)

        produtor2 = Produtor(
            cpf_cnpj="98765432100",
            nome="Maria Oliveira Costa"
        )
        db.add(produtor2)
        db.flush()

        fazenda3 = Fazenda(
            nome="Fazenda São João",
            cidade="Goiânia",
            estado="GO",
            area_total=2000.0,
            area_agricultavel=1600.0,
            area_vegetacao=400.0,
            produtor_id=produtor2.id
        )
        db.add(fazenda3)
        db.flush()

        cultura4 = Cultura(
            nome="Soja",
            safra="2023",
            fazenda_id=fazenda3.id
        )
        cultura5 = Cultura(
            nome="Algodão",
            safra="2023",
            fazenda_id=fazenda3.id
        )
        db.add_all([cultura4, cultura5])

        produtor3 = Produtor(
            cpf_cnpj="11222333000181",
            nome="Agropecuária Brasil Ltda"
        )
        db.add(produtor3)
        db.flush()

        fazenda4 = Fazenda(
            nome="Fazenda Industrial",
            cidade="Londrina",
            estado="PR",
            area_total=3000.0,
            area_agricultavel=2400.0,
            area_vegetacao=600.0,
            produtor_id=produtor3.id
        )
        db.add(fazenda4)
        db.flush()

        cultura6 = Cultura(
            nome="Soja",
            safra="2023",
            fazenda_id=fazenda4.id
        )
        cultura7 = Cultura(
            nome="Trigo",
            safra="2023",
            fazenda_id=fazenda4.id
        )
        cultura8 = Cultura(
            nome="Milho",
            safra="2023",
            fazenda_id=fazenda4.id
        )
        db.add_all([cultura6, cultura7, cultura8])

        db.commit()
        logger.info("Dados de exemplo criados com sucesso!")

    except Exception as e:
        logger.error(f"Erro ao criar dados de exemplo: {e}")
        db.rollback()
    finally:
        db.close() 