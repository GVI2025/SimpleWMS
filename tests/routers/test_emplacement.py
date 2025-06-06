from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, ANY

from app.schemas.emplacement import EmplacementCreate, EmplacementUpdate, EmplacementRead, TypeEmplacement
from app.models import Emplacement as EmplacementModel

client = TestClient(app)

mock_emplacement_data = {
    "id": "12345",
    "code": "EMPL001",
    "type": TypeEmplacement.STOCKAGE.value,
    "capacite_poids_kg": 1000.0,
    "capacite_volume_m3": 10.0
}

mock_emplacement_create = EmplacementCreate(
    code="EMPL001",
    type=TypeEmplacement.STOCKAGE.value,
    capacite_poids_kg=1000.0,
    capacite_volume_m3=10.0
)

mock_emplacement_update = EmplacementUpdate(
    code="EMPL001",
    type=TypeEmplacement.STOCKAGE.value,
    capacite_poids_kg=2000.0,
    capacite_volume_m3=20.0
)

mock_emplacement_model = EmplacementModel(
    id="12345",
    code="EMPL001",
    type=TypeEmplacement.STOCKAGE.value,
    capacite_poids_kg=1000.0,
    capacite_volume_m3=10.0
)

mock_emplacement_list = [
    EmplacementModel(
        id="12345",
        code="EMPL001",
        type=TypeEmplacement.STOCKAGE.value,
        capacite_poids_kg=1000.0,
        capacite_volume_m3=10.0
    ),
    EmplacementModel(
        id="E67890",
        code="EMPL002",
        type=TypeEmplacement.VENTE.value,
        capacite_poids_kg=500.0,
        capacite_volume_m3=5.0
    )
]

class TestEmplacementRouter:
    @patch('app.routers.emplacement.emplacement_service.list_emplacements')
    def test_list_emplacements(self, mock_list):
        mock_list.return_value = mock_emplacement_list 

        response = client.get("/emplacements/")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]['code'] == "EMPL001"
        assert response.json()[1]['code'] == "EMPL002"

        mock_list.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.create_emplacement')
    def test_create_emplacement_success(self, mock_create):
        mock_create.return_value = mock_emplacement_model

        response = client.post("/emplacements/", json={
            "code": mock_emplacement_create.code,
            "type": mock_emplacement_create.type,
            "capacite_poids_kg": mock_emplacement_create.capacite_poids_kg,
            "capacite_volume_m3": mock_emplacement_create.capacite_volume_m3
        })
        assert response.status_code == 200
        assert response.json()["code"] == mock_emplacement_create.code
        assert response.json()["type"] == mock_emplacement_create.type
        assert response.json()["capacite_poids_kg"] == mock_emplacement_create.capacite_poids_kg
        assert response.json()["capacite_volume_m3"] == mock_emplacement_create.capacite_volume_m3

        mock_create.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_success(self, mock_get):
        mock_get.return_value = mock_emplacement_model

        response = client.get("/emplacements/12345")
        assert response.status_code == 200
        assert response.json()["code"] == "EMPL001"
        assert response.json()["type"] == TypeEmplacement.STOCKAGE.value

        mock_get.assert_called_once_with(ANY, "12345")

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_success(self, mock_update):
        mock_update.return_value = mock_emplacement_model

        response = client.put("/emplacements/12345", json=mock_emplacement_update.dict())
        assert response.status_code == 200
        assert response.json()["code"] == mock_emplacement_update.code
        assert response.json()["type"] == mock_emplacement_update.type
        assert response.json()["capacite_poids_kg"] == mock_emplacement_update.capacite_poids_kg
        assert response.json()["capacite_volume_m3"] == mock_emplacement_update.capacite_volume_m3

        mock_update.assert_called_once_with(ANY, "12345", mock_emplacement_update)

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_success(self, mock_delete):
        mock_delete.return_value = None

        response = client.delete("/emplacements/12345")
        assert response.status_code == 204

        mock_delete.assert_called_once_with(ANY, "12345")

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_not_found(self, mock_get):
        mock_get.return_value = None

        response = client.get("/emplacements/nonexistent")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

        mock_get.assert_called_once_with(ANY, "nonexistent")

    @patch('app.routers.emplacement.emplacement_service.create_emplacement')
    def test_create_emplacement_already_exists(self, mock_create):
        mock_create.side_effect = Exception("Emplacement with this code already exists.")

        response = client.post("/emplacements/", json=mock_emplacement_create.dict())
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

        mock_create.assert_called_once()

