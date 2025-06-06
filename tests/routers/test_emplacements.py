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
        id="1",
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

    ''' @patch('app.routers.emplacement.emplacement_service.create_emplacement')
    def test_create_emplacement_success(self, mock_create_emplacement):
        # Configure mock
        mock_create_emplacement.return_value = mock_emplacement_model

        # Test the endpoint
        response = client.post("/emplacements/", json={
            "article_id": "A12345",
            "emplacement_id": "E12345",
            "quantite": 50,
            "seuil_minimum": 10
        })

        # Verify response
        assert response.status_code == 200
        assert response.json()["article_id"] == "A12345"
        assert response.json()["quantite"] == 50

        # Verify service function was called correctly
        mock_create_emplacement.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_success(self, mock_get_emplacement):
        # Configure mock
        mock_get_emplacement.return_value = mock_emplacement_model

        # Test the endpoint
        response = client.get(f"/emplacements/{mock_emplacement_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_emplacement_data["id"]

        # Verify service function was called correctly
        mock_get_emplacement.assert_called_once_with(ANY, mock_emplacement_data["id"])

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_not_found(self, mock_get_emplacement):
        # Configure mock
        mock_get_emplacement.return_value = None

        # Test the endpoint
        response = client.get("/emplacements/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_success(self, mock_update_emplacement):
        # Configure mock
        updated_emplacement = mock_emplacement_model
        updated_emplacement.quantite = 75
        updated_emplacement.seuil_minimum = 15
        mock_update_emplacement.return_value = updated_emplacement

        # Test the endpoint
        response = client.put(
            f"/emplacements/{mock_emplacement_data['id']}",
            json={
                "article_id": "A12345",
                "emplacement_id": "E12345",
                "quantite": 75,
                "seuil_minimum": 15
            }
        )

        # Verify response
        assert response.status_code == 200
        assert response.json()["quantite"] == 75
        assert response.json()["seuil_minimum"] == 15

        # Verify service function was called correctly
        mock_update_emplacement.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_not_found(self, mock_update_emplacement):
        # Configure mock
        mock_update_emplacement.return_value = None

        # Test the endpoint
        response = client.put(
            "/emplacements/nonexistent",
            json={
                "article_id": "A12345",
                "emplacement_id": "E12345",
                "quantite": 75,
                "seuil_minimum": 15
            }
        )

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_success(self, mock_delete_emplacement):
        # Configure mock
        mock_delete_emplacement.return_value = mock_emplacement_model

        # Test the endpoint
        response = client.delete(f"/emplacements/{mock_emplacement_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_emplacement_data["id"]

        # Verify service function was called correctly
        mock_delete_emplacement.assert_called_once_with(ANY, mock_emplacement_data["id"])

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_not_found(self, mock_delete_emplacement):
        # Configure mock
        mock_delete_emplacement.return_value = None

        # Test the endpoint
        response = client.delete("/emplacements/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"] '''