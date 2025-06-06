from fastapi.testclient import TestClient
from unittest.mock import patch, ANY

from app.main import app
from app.schemas.emplacement import EmplacementCreate, EmplacementUpdate, TypeEmplacement
from app.models import Emplacement as EmplacementModel

client = TestClient(app)

# Mock emplacement data
mock_emplacement_data = {
    "id" :"1",
    "code": "E123",
    "type": TypeEmplacement.STOCKAGE.value,
    "capacite_poids_kg": 1000.0,
    "capacite_volume_m3": 50.0
}

mock_emplacement_create = EmplacementCreate(
    code="E123",
    type=TypeEmplacement.STOCKAGE.value,
    capacite_poids_kg=1000.0,
    capacite_volume_m3=50.0
)

mock_emplacement_update = EmplacementUpdate(
    code="E123",
    type=TypeEmplacement.STOCKAGE.value,
    capacite_poids_kg=1000.0,
    capacite_volume_m3=75.0
)

mock_emplacement_model = EmplacementModel(
    id="E123",
    code="E123",
    type="Zone de stockage",
    capacite_poids_kg=500.0,
    capacite_volume_m3=3.0
)

mock_emplacement_list = [
    EmplacementModel(
        id="1",
        code="E123",
        type=TypeEmplacement.STOCKAGE.value,
        capacite_poids_kg=1000,
        capacite_volume_m3=3.0
    ),
    EmplacementModel(
        id="2",
        code="E123",
        type=TypeEmplacement.STOCKAGE.value,
        capacite_poids_kg=1000,
        capacite_volume_m3=50.0
    ),
]


class TestEmplacementRouter:
    @patch('app.routers.emplacement.emplacement_service.list_emplacements')
    def test_list_emplacements(self, mock_list_emplacements):
        mock_list_emplacements.return_value = mock_emplacement_list
        response = client.get("/emplacements/")
        assert response.status_code == 200
        assert len(response.json()) == 2
        mock_list_emplacements.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement_by_code')
    @patch('app.routers.emplacement.emplacement_service.create_emplacement')
    def test_create_emplacement_success(self, mock_create_emplacement, mock_get_by_code):
        mock_get_by_code.return_value = None
        mock_create_emplacement.return_value = mock_emplacement_model
        response = client.post("/emplacements/", json=mock_emplacement_create.dict())
        assert response.status_code == 200
        assert response.json()["code"] == "E123"
        mock_create_emplacement.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement_by_code')
    def test_create_emplacement_duplicate(self, mock_get_by_code):
        mock_get_by_code.return_value = mock_emplacement_model
        response = client.post("/emplacements/", json=mock_emplacement_create.dict())
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_success(self, mock_get_emplacement):
        mock_get_emplacement.return_value = mock_emplacement_model
        response = client.get(f"/emplacements/{mock_emplacement_data['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == "E123"
        mock_get_emplacement.assert_called_once_with(ANY, "E123")

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_not_found(self, mock_get_emplacement):
        mock_get_emplacement.return_value = None
        response = client.get("/emplacements/nonexistent")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_success(self, mock_update_emplacement):
        updated = mock_emplacement_model
        updated.capacite_poids_kg = 1000.0
        updated.capacite_volume_m3 = 6.0
        mock_update_emplacement.return_value = updated
        response = client.put(
            f"/emplacements/{mock_emplacement_data['id']}",
            json=mock_emplacement_update.dict()
        )
        assert response.status_code == 200
        assert response.json()["capacite_poids_kg"] == 1000.0
        mock_update_emplacement.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_not_found(self, mock_update_emplacement):
        mock_update_emplacement.return_value = None
        response = client.put(
            "/emplacements/nonexistent",
            json=mock_emplacement_update.dict()
        )
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_success(self, mock_delete_emplacement):
        mock_delete_emplacement.return_value = mock_emplacement_model
        response = client.delete(f"/emplacements/{mock_emplacement_data['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == "E123"
        mock_delete_emplacement.assert_called_once_with(ANY, "E123")

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_not_found(self, mock_delete_emplacement):
        mock_delete_emplacement.return_value = None
        response = client.delete("/emplacements/nonexistent")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]