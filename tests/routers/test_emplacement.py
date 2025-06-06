import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from uuid import uuid4

from app.main import app
from app.schemas.emplacement import Emplacement, EmplacementCreate, EmplacementUpdate

client = TestClient(app)

# Mock data for testing
mock_emplacement_id = str(uuid4())
mock_emplacement = Emplacement(
    id=mock_emplacement_id,
    code="A01",
    allée=1,
    colonne=2,
    niveau=3,
    zone="STOCK"
)

mock_emplacement_list = [
    mock_emplacement,
    Emplacement(
        id=str(uuid4()),
        code="B02",
        allée=2, 
        colonne=3,
        niveau=1,
        zone="RECEPTION"
    )
]

class TestEmplacementRouter:
    
    @patch('app.routers.emplacement.emplacement_service.list_emplacements')
    def test_read_emplacements(self, mock_list_emplacements):
        mock_list_emplacements.return_value = mock_emplacement_list
        
        response = client.get("/emplacements/")
        
        assert response.status_code == 200
        assert len(response.json()) == len(mock_emplacement_list)
        mock_list_emplacements.assert_called_once()
    
    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_read_emplacement(self, mock_get_emplacement):
        mock_get_emplacement.return_value = mock_emplacement
        
        response = client.get(f"/emplacements/{mock_emplacement_id}")
        
        assert response.status_code == 200
        assert response.json()["id"] == mock_emplacement_id
        mock_get_emplacement.assert_called_once_with(pytest.ANY, mock_emplacement_id)
    
    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_read_emplacement_not_found(self, mock_get_emplacement):
        mock_get_emplacement.return_value = None
        
        response = client.get(f"/emplacements/{mock_emplacement_id}")
        
        assert response.status_code == 404
        mock_get_emplacement.assert_called_once()
    
    @patch('app.routers.emplacement.emplacement_service.create_emplacement')
    def test_create_emplacement(self, mock_create_emplacement):
        mock_create_emplacement.return_value = mock_emplacement
        
        emplacement_data = {
            "code": "A01",
            "allée": 1,
            "colonne": 2,
            "niveau": 3,
            "zone": "STOCK"
        }
        
        response = client.post("/emplacements/", json=emplacement_data)
        
        assert response.status_code == 201
        assert response.json()["code"] == emplacement_data["code"]
        mock_create_emplacement.assert_called_once()
    
    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement(self, mock_update_emplacement):
        mock_update_emplacement.return_value = mock_emplacement
        
        update_data = {
            "code": "A01-Updated",
            "zone": "EXPEDITION"
        }
        
        response = client.put(f"/emplacements/{mock_emplacement_id}", json=update_data)
        
        assert response.status_code == 200
        mock_update_emplacement.assert_called_once()
    
    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_not_found(self, mock_update_emplacement):
        mock_update_emplacement.return_value = None
        
        update_data = {"code": "A01-Updated"}
        
        response = client.put(f"/emplacements/{mock_emplacement_id}", json=update_data)
        
        assert response.status_code == 404
        mock_update_emplacement.assert_called_once()
    
    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement(self, mock_delete_emplacement):
        mock_delete_emplacement.return_value = mock_emplacement
        
        response = client.delete(f"/emplacements/{mock_emplacement_id}")
        
        assert response.status_code == 200
        mock_delete_emplacement.assert_called_once_with(pytest.ANY, mock_emplacement_id)
    
    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_not_found(self, mock_delete_emplacement):
        mock_delete_emplacement.return_value = None
        
        response = client.delete(f"/emplacements/{mock_emplacement_id}")
        
        assert response.status_code == 404
        mock_delete_emplacement.assert_called_once()