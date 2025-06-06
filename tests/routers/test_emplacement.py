from fastapi.testclient import TestClient
from unittest.mock import patch, ANY

from app.main import app
from app.schemas.emplacement import EmplacementCreate, EmplacementUpdate, TypeEmplacement
from app.models import Emplacement as EmplacementModel

client = TestClient(app)

# Mock emplacement data
mock_emplacement_data = {
    "id": "12345",
    "code": "E001",
    "type": TypeEmplacement.STOCKAGE,
    "capacite_poids_kg": 1000.0,
    "capacite_volume_m3": 10.0
}

mock_emplacement_create = EmplacementCreate(
    code="E001",
    type=TypeEmplacement.STOCKAGE,
    capacite_poids_kg=1000.0,
    capacite_volume_m3=10.0
)

mock_emplacement_update = EmplacementUpdate(
    code="E001",
    type=TypeEmplacement.RESERVATION,
    capacite_poids_kg=1500.0,
    capacite_volume_m3=15.0
)

mock_emplacement_model = EmplacementModel(
    id="12345",
    code="E001",
    type=TypeEmplacement.STOCKAGE,
    capacite_poids_kg=1000.0,
    capacite_volume_m3=10.0
)

mock_emplacement_list = [
    EmplacementModel(
        id="12345",
        code="E001",
        type=TypeEmplacement.STOCKAGE,
        capacite_poids_kg=1000.0,
        capacite_volume_m3=10.0
    ),
    EmplacementModel(
        id="67890",
        code="E002",
        type=TypeEmplacement.EXPEDITION,
        capacite_poids_kg=500.0,
        capacite_volume_m3=5.0
    )
]


class TestEmplacementRouter:
    @patch('app.routers.emplacement.emplacement_service.list_emplacements')
    def test_list_emplacements(self, mock_list_emplacements):
        # Configure mock
        mock_list_emplacements.return_value = mock_emplacement_list

        # Test the endpoint
        response = client.get("/emplacements/")

        # Verify response
        assert response.status_code == 200
        assert len(response.json()) == 2

        # Verify service function was called
        mock_list_emplacements.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement_by_code')
    @patch('app.routers.emplacement.emplacement_service.create_emplacement')
    def test_create_emplacement_success(self, mock_create_emplacement, mock_get_by_code):
        # Configure mocks
        mock_get_by_code.return_value = None
        mock_create_emplacement.return_value = mock_emplacement_model

        # Test the endpoint
        response = client.post("/emplacements/", json={
            "code": "E001",
            "type": "Zone de stockage",
            "capacite_poids_kg": 1000.0,
            "capacite_volume_m3": 10.0
        })

        # Verify response
        assert response.status_code == 200
        assert response.json()["code"] == "E001"
        assert response.json()["type"] == "Zone de stockage"
        assert response.json()["capacite_poids_kg"] == 1000.0

        # Verify service functions were called correctly
        mock_get_by_code.assert_called_once_with(ANY, "E001")
        mock_create_emplacement.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement_by_code')
    def test_create_emplacement_duplicate_code(self, mock_get_by_code):
        # Configure mock to simulate duplicate code
        mock_get_by_code.return_value = mock_emplacement_model

        # Test the endpoint
        response = client.post("/emplacements/", json={
            "code": "E001",
            "type": "Zone de stockage",
            "capacite_poids_kg": 1000.0,
            "capacite_volume_m3": 10.0
        })

        # Verify response
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

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
        updated_emplacement.type = TypeEmplacement.RESERVATION
        updated_emplacement.capacite_poids_kg = 1500.0
        mock_update_emplacement.return_value = updated_emplacement

        # Test the endpoint
        response = client.put(
            f"/emplacements/{mock_emplacement_data['id']}",
            json={
                "code": "E001",
                "type": "Zone de réservation",
                "capacite_poids_kg": 1500.0,
                "capacite_volume_m3": 15.0
            }
        )

        # Verify response
        assert response.status_code == 200
        assert response.json()["type"] == "Zone de réservation"
        assert response.json()["capacite_poids_kg"] == 1500.0

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
                "code": "E001",
                "type": "Zone de réservation",
                "capacite_poids_kg": 1500.0,
                "capacite_volume_m3": 15.0
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
        assert "not found" in response.json()["detail"]
