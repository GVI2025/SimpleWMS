from fastapi.testclient import TestClient
from unittest.mock import patch, ANY

from app.main import app
from app.schemas.emplacement import TypeEmplacement, EmplacementCreate, EmplacementUpdate
from app.models import Emplacement as EmplacementModel

client = TestClient(app)

# Données mock
mock_emplacement_data = {
    "id": "e123",
    "code": "A1-B2",
    "type": "Zone de stockage",
    "capacite_poids_kg": 1500.0,
    "capacite_volume_m3": 12.5
}

mock_emplacement_create = EmplacementCreate(
    code="A1-B2",
    type=TypeEmplacement.STOCKAGE,
    capacite_poids_kg=1500.0,
    capacite_volume_m3=12.5
)

mock_emplacement_update = EmplacementUpdate(
    code="A1-B2",
    type=TypeEmplacement.VENTE,
    capacite_poids_kg=1000.0,
    capacite_volume_m3=10.0
)

mock_emplacement_model = EmplacementModel(
    id="e123",
    code="A1-B2",
    type=TypeEmplacement.STOCKAGE,
    capacite_poids_kg=1500.0,
    capacite_volume_m3=12.5
)

mock_emplacement_list = [
    EmplacementModel(
        id="e123", code="A1-B2", type=TypeEmplacement.STOCKAGE,
        capacite_poids_kg=1500.0, capacite_volume_m3=12.5
    ),
    EmplacementModel(
        id="e456", code="C3-D4", type=TypeEmplacement.VENTE,
        capacite_poids_kg=800.0, capacite_volume_m3=7.0
    )
]


class TestEmplacementRouter:
    @patch('app.routers.emplacement.emplacement_service.list_emplacements')
    def test_list_emplacements(self, mock_list):
        mock_list.return_value = mock_emplacement_list

        response = client.get("/emplacements/")
        assert response.status_code == 200
        assert len(response.json()) == 2
        mock_list.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement_by_code')
    @patch('app.routers.emplacement.emplacement_service.create_emplacement')
    def test_create_emplacement_success(self, mock_create, mock_get_by_code):
        mock_get_by_code.return_value = None
        mock_create.return_value = mock_emplacement_model

        response = client.post("/emplacements/", json={
            "code": "A1-B2",
            "type": "Zone de stockage",
            "capacite_poids_kg": 1500.0,
            "capacite_volume_m3": 12.5
        })

        assert response.status_code == 200
        assert response.json()["code"] == mock_emplacement_data["code"]
        mock_get_by_code.assert_called_once_with(ANY, mock_emplacement_data["code"])
        mock_create.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement_by_code')
    def test_create_emplacement_duplicate_code(self, mock_get_by_code):
        mock_get_by_code.return_value = mock_emplacement_model

        response = client.post("/emplacements/", json={
            "code": "A1-B2",
            "type": "Zone de stockage",
            "capacite_poids_kg": 1500.0,
            "capacite_volume_m3": 12.5
        })

        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_success(self, mock_get):
        mock_get.return_value = mock_emplacement_model

        response = client.get("/emplacements/e123")
        assert response.status_code == 200
        assert response.json()["id"] == mock_emplacement_data["id"]
        mock_get.assert_called_once_with(ANY, "e123")

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_not_found(self, mock_get):
        mock_get.return_value = None

        response = client.get("/emplacements/invalid-id")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_success(self, mock_update):
        updated_model = mock_emplacement_model
        updated_model.type = TypeEmplacement.VENTE
        updated_model.capacite_poids_kg = 1000.0
        updated_model.capacite_volume_m3 = 10.0
        mock_update.return_value = updated_model

        response = client.put("/emplacements/e123", json={
            "code": "A1-B2",
            "type": "Surface de vente",
            "capacite_poids_kg": 1000.0,
            "capacite_volume_m3": 10.0
        })

        assert response.status_code == 200
        assert response.json()["type"] == "Surface de vente"
        mock_update.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_not_found(self, mock_update):
        mock_update.return_value = None

        response = client.put("/emplacements/invalid-id", json={
            "code": "A1-B2",
            "type": "Surface de vente",
            "capacite_poids_kg": 1000.0,
            "capacite_volume_m3": 10.0
        })

        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_success(self, mock_delete):
        mock_delete.return_value = mock_emplacement_model

        response = client.delete("/emplacements/e123")
        assert response.status_code == 200
        assert response.json()["id"] == mock_emplacement_data["id"]
        mock_delete.assert_called_once_with(ANY, "e123")

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_not_found(self, mock_delete):
        mock_delete.return_value = None

        response = client.delete("/emplacements/invalid-id")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]
