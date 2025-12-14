"""Tests básicos de salud de la API"""
import pytest


@pytest.mark.integration
def test_read_root(client):
    """Test del endpoint raíz"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Welcome to TaskAPI"


@pytest.mark.integration
def test_docs_endpoint(client):
    """Test que el endpoint de documentación existe"""
    response = client.get("/docs")
    assert response.status_code == 200