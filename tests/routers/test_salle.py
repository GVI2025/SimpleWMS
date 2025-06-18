from fastapi.testclient import TestClient
from unittest.mock import patch, ANY
from datetime import datetime

from app.main import app
from app.schemas.salle import SalleCreate, SalleUpdate
from app.models import Salle as SalleModel

client = TestClient(app)

mock_salle_data = {
    "id": "test_id",
    "nom": "Test Salle",
    "capacité": 100,
    "localisation": "Test Localisation",
}

mock_salle_create = SalleCreate(
    nom="Test Salle",
    capacité=100,
    localisation="Test Localisation",
)

mock_salle_update = SalleUpdate(
    nom="Updated Salle",
    capacité=150,
    localisation="Updated Localisation",
)

class TestSalleRouter:
    @patch("app.services.salle.list_salles")
    def test_list_salle(self, mock_get_all_salles):
        mock_get_all_salles.return_value = [mock_salle_data]
        response = client.get("/salles/")
        assert response.status_code == 200
        assert response.json() == [mock_salle_data]

    @patch("app.services.salle.get_salle")
    def test_get_salle(self, mock_get_salle_by_id):
        mock_get_salle_by_id.return_value = mock_salle_data
        response = client.get("/salles/test_id")
        assert response.status_code == 200
        assert response.json() == mock_salle_data

    @patch("app.services.salle.get_salle_by_name")
    def test_get_salle_by_name(self, mock_get_salle_by_name):
        mock_get_salle_by_name.return_value = mock_salle_data
        response = client.get("/salles/name/Test%20Salle")
        assert response.status_code == 200
        assert response.json() == mock_salle_data

    @patch("app.services.salle.create_salle")
    def test_create_salle(self, mock_create_salle):
        mock_create_salle.return_value = mock_salle_data
        response = client.post("/salles/", json=mock_salle_create.model_dump())
        assert response.status_code == 200
        assert response.json() == mock_salle_data

    # @patch("app.services.salle.update_salle")
    # def test_update_salle(self, mock_update_salle):
    #     updated_salle = mock_salle_data.copy()
    #     print("Updated Salle:", updated_salle)
    #     updated_salle["nom"] = "Updated Salle"
    #     # updated_salle["capacité"] = 150
    #     # updated_salle["localisation"] = "Updated Localisation"
    #     mock_update_salle.return_value = mock_salle_data

    #     # Test the update endpoint
    #     response = client.put("/salles/test_id", json=mock_salle_update.model_dump())

    #     assert response.status_code == 200

    @patch("app.services.salle.delete_salle")
    def test_delete_salle(self, mock_delete_salle):
        mock_delete_salle.return_value = mock_salle_data
        response = client.delete("/salles/test_id")
        assert response.status_code == 200