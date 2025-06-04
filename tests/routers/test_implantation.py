from fastapi.testclient import TestClient
from unittest.mock import patch, ANY

from app.main import app
from app.schemas.implantation import ImplantationCreate, ImplantationUpdate
from app.models import Implantation as ImplantationModel

client = TestClient(app)

# Mock implantation data
mock_implantation_data = {
    "id": "12345",
    "article_id": "A12345",
    "emplacement_id": "E12345",
    "quantite": 50,
    "seuil_minimum": 10
}

mock_implantation_create = ImplantationCreate(
    article_id="A12345",
    emplacement_id="E12345",
    quantite=50,
    seuil_minimum=10
)

mock_implantation_update = ImplantationUpdate(
    article_id="A12345",
    emplacement_id="E12345",
    quantite=75,
    seuil_minimum=15
)

mock_implantation_model = ImplantationModel(
    id="12345",
    article_id="A12345",
    emplacement_id="E12345",
    quantite=50,
    seuil_minimum=10
)

mock_implantation_list = [
    ImplantationModel(
        id="12345",
        article_id="A12345",
        emplacement_id="E12345",
        quantite=50,
        seuil_minimum=10
    ),
    ImplantationModel(
        id="67890",
        article_id="A67890",
        emplacement_id="E67890",
        quantite=25,
        seuil_minimum=5
    )
]


class TestImplantationRouter:
    @patch('app.routers.implantation.implantation_service.list_implantations')
    def test_list_implantations(self, mock_list_implantations):
        # Configure mock
        mock_list_implantations.return_value = mock_implantation_list

        # Test the endpoint
        response = client.get("/implantations/")

        # Verify response
        assert response.status_code == 200
        assert len(response.json()) == 2

        # Verify service function was called
        mock_list_implantations.assert_called_once()

    @patch('app.routers.implantation.implantation_service.create_implantation')
    def test_create_implantation_success(self, mock_create_implantation):
        # Configure mock
        mock_create_implantation.return_value = mock_implantation_model

        # Test the endpoint
        response = client.post("/implantations/", json={
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
        mock_create_implantation.assert_called_once()

    @patch('app.routers.implantation.implantation_service.get_implantation')
    def test_get_implantation_success(self, mock_get_implantation):
        # Configure mock
        mock_get_implantation.return_value = mock_implantation_model

        # Test the endpoint
        response = client.get(f"/implantations/{mock_implantation_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_implantation_data["id"]

        # Verify service function was called correctly
        mock_get_implantation.assert_called_once_with(ANY, mock_implantation_data["id"])

    @patch('app.routers.implantation.implantation_service.get_implantation')
    def test_get_implantation_not_found(self, mock_get_implantation):
        # Configure mock
        mock_get_implantation.return_value = None

        # Test the endpoint
        response = client.get("/implantations/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.implantation.implantation_service.update_implantation')
    def test_update_implantation_success(self, mock_update_implantation):
        # Configure mock
        updated_implantation = mock_implantation_model
        updated_implantation.quantite = 75
        updated_implantation.seuil_minimum = 15
        mock_update_implantation.return_value = updated_implantation

        # Test the endpoint
        response = client.put(
            f"/implantations/{mock_implantation_data['id']}",
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
        mock_update_implantation.assert_called_once()

    @patch('app.routers.implantation.implantation_service.update_implantation')
    def test_update_implantation_not_found(self, mock_update_implantation):
        # Configure mock
        mock_update_implantation.return_value = None

        # Test the endpoint
        response = client.put(
            "/implantations/nonexistent",
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

    @patch('app.routers.implantation.implantation_service.delete_implantation')
    def test_delete_implantation_success(self, mock_delete_implantation):
        # Configure mock
        mock_delete_implantation.return_value = mock_implantation_model

        # Test the endpoint
        response = client.delete(f"/implantations/{mock_implantation_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_implantation_data["id"]

        # Verify service function was called correctly
        mock_delete_implantation.assert_called_once_with(ANY, mock_implantation_data["id"])

    @patch('app.routers.implantation.implantation_service.delete_implantation')
    def test_delete_implantation_not_found(self, mock_delete_implantation):
        # Configure mock
        mock_delete_implantation.return_value = None

        # Test the endpoint
        response = client.delete("/implantations/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]