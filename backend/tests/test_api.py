import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db
from app.models import Base
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_produtor():
    """Teste para criar um produtor"""
    produtor_data = {
        "cpf_cnpj": "12345678909",  # CPF válido
        "nome": "João Silva",
        "fazendas": []
    }
    
    response = client.post("/api/v1/produtores/", json=produtor_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["nome"] == "João Silva"
    assert data["cpf_cnpj"] == "12345678909"
    assert "id" in data

def test_create_produtor_with_fazenda():
    """Teste para criar um produtor com fazenda"""
    produtor_data = {
        "cpf_cnpj": "98765432100",  # CPF válido
        "nome": "Maria Santos",
        "fazendas": [
            {
                "nome": "Fazenda Santa Maria",
                "cidade": "São Paulo",
                "estado": "SP",
                "area_total": 1000.0,
                "area_agricultavel": 800.0,
                "area_vegetacao": 200.0,
                "culturas": [
                    {"nome": "Soja", "safra": "2023"},
                    {"nome": "Milho", "safra": "2023"}
                ]
            }
        ]
    }
    
    response = client.post("/api/v1/produtores/", json=produtor_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["nome"] == "Maria Santos"
    assert len(data["fazendas"]) == 1
    assert data["fazendas"][0]["nome"] == "Fazenda Santa Maria"
    assert len(data["fazendas"][0]["culturas"]) == 2

def test_duplicate_cpf_cnpj():
    """Teste para CPF/CNPJ duplicado"""
    produtor_data = {
        "cpf_cnpj": "12345678909",  # CPF válido
        "nome": "João Silva",
        "fazendas": []
    }
    
    # Criar primeiro produtor
    response = client.post("/api/v1/produtores/", json=produtor_data)
    assert response.status_code == 201
    
    # Tentar criar segundo produtor com mesmo CPF
    response = client.post("/api/v1/produtores/", json=produtor_data)
    assert response.status_code == 400
    assert "CPF/CNPJ já cadastrado" in response.json()["detail"]

def test_invalid_cpf():
    """Teste para CPF inválido"""
    produtor_data = {
        "cpf_cnpj": "12345678900",  # CPF inválido
        "nome": "João Silva",
        "fazendas": []
    }
    
    response = client.post("/api/v1/produtores/", json=produtor_data)
    assert response.status_code == 422

def test_area_validation():
    """Teste para validação de áreas"""
    produtor_data = {
        "cpf_cnpj": "11222333000181",  # CNPJ válido
        "nome": "João Silva",
        "fazendas": [
            {
                "nome": "Fazenda Teste",
                "cidade": "São Paulo",
                "estado": "SP",
                "area_total": 1000.0,
                "area_agricultavel": 800.0,
                "area_vegetacao": 300.0,  # Soma > área total
                "culturas": []
            }
        ]
    }
    
    response = client.post("/api/v1/produtores/", json=produtor_data)
    assert response.status_code == 422

def test_get_produtores():
    """Teste para listar produtores"""
    # Criar produtor
    produtor_data = {
        "cpf_cnpj": "11222333000181",  # CNPJ válido
        "nome": "João Silva",
        "fazendas": []
    }
    client.post("/api/v1/produtores/", json=produtor_data)
    
    # Listar produtores
    response = client.get("/api/v1/produtores/")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) >= 1

def test_dashboard_stats():
    """Teste para estatísticas do dashboard"""
    # Criar produtor com fazenda
    produtor_data = {
        "cpf_cnpj": "11222333000181",  # CNPJ válido
        "nome": "João Silva",
        "fazendas": [
            {
                "nome": "Fazenda Teste",
                "cidade": "São Paulo",
                "estado": "SP",
                "area_total": 1000.0,
                "area_agricultavel": 800.0,
                "area_vegetacao": 200.0,
                "culturas": [
                    {"nome": "Soja", "safra": "2023"}
                ]
            }
        ]
    }
    client.post("/api/v1/produtores/", json=produtor_data)
    
    # Obter estatísticas
    response = client.get("/api/v1/dashboard/")
    assert response.status_code == 200
    
    data = response.json()
    assert data["total_fazendas"] >= 1
    assert data["total_hectares"] >= 1000.0
    assert "SP" in data["por_estado"]
    assert "Soja" in data["por_cultura"]
    assert "Área Agricultável" in data["por_uso_solo"]
    assert "Área de Vegetação" in data["por_uso_solo"] 