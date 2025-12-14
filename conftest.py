import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base, get_db
from main import app

# Configurar base de datos de prueba en memoria
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override de la dependencia de base de datos para tests"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def test_db():
    """Fixture que crea y destruye la base de datos para cada test"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(test_db):
    """Fixture que provee un cliente de testing de FastAPI"""
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def sample_task_data():
    """Fixture con datos de ejemplo para tests"""
    return {
        "title": "Test Task",
        "description": "This is a test task",
        "status": "pending",
        "category": "work"
    }


@pytest.fixture
def create_task(client, sample_task_data):
    """Fixture que crea una tarea de prueba y retorna sus datos"""
    response = client.post("/tasks", json=sample_task_data)
    return response.json()