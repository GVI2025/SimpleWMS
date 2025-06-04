from fastapi.testclient import TestClient
from unittest.mock import patch, ANY
from datetime import datetime

from app.main import app
from app.schemas.reception import ReceptionCreate, ReceptionUpdate
from app.models import Reception as ReceptionModel

client = TestClient(app)

# Mock reception data
current_datetime = datetime.now()

mock_reception_data = {
    "id": "12345",
    "article_id": "A12345",
    "quantite": 50,
    "fournisseur": "Fournisseur Test",
    "date_reception": current_datetime,
    "emplacement_id": "E12345"
}

mock_reception_create = ReceptionCreate(
    article_id="A12345",
    quantite=50,
    fournisseur="Fournisseur Test",
    date_reception=current_datetime,
    emplacement_id="E12345"
)

mock_reception_update = ReceptionUpdate(
    article_id="A12345",
    quantite=75,
    fournisseur="Fournisseur Test Updated",
    date_reception=current_datetime,
    emplacement_id="E12345"
)

mock_reception_model = ReceptionModel(
    id="12345",
    article_id="A12345",
    quantite=50,
    fournisseur="Fournisseur Test",
    date_reception=current_datetime,
    emplacement_id="E12345"
)

mock_reception_list = [
    ReceptionModel(
        id="12345",
        article_id="A12345",
        quantite=50,
        fournisseur="Fournisseur Test",
        date_reception=current_datetime,
        emplacement_id="E12345"
    ),
    ReceptionModel(
        id="67890",
        article_id="A67890",
        quantite=25,
        fournisseur="Autre Fournisseur",
        date_reception=current_datetime,
        emplacement_id="E67890"
    )
]


class TestReceptionRouter:
    @patch('app.routers.reception.reception_service.list_receptions')
    def test_list_receptions(self, mock_list_receptions):
        # Configure mock
        mock_list_receptions.return_value = mock_reception_list

        # Test the endpoint
        response = client.get("/receptions/")

        # Verify response
        assert response.status_code == 200
        assert len(response.json()) == 2

        # Verify service function was called
        mock_list_receptions.assert_called_once()

    @patch('app.routers.reception.reception_service.create_reception')
    def test_create_reception_success(self, mock_create_reception):
        # Configure mock
        mock_create_reception.return_value = mock_reception_model

        # Test the endpoint
        response = client.post("/receptions/", json={
            "article_id": "A12345",
            "quantite": 50,
            "fournisseur": "Fournisseur Test",
            "date_reception": current_datetime.isoformat(),
            "emplacement_id": "E12345"
        })

        # Verify response
        assert response.status_code == 200
        assert response.json()["article_id"] == "A12345"
        assert response.json()["quantite"] == 50
        assert response.json()["fournisseur"] == "Fournisseur Test"

        # Verify service function was called correctly
        mock_create_reception.assert_called_once()

    @patch('app.routers.reception.reception_service.get_reception')
    def test_get_reception_success(self, mock_get_reception):
        # Configure mock
        mock_get_reception.return_value = mock_reception_model

        # Test the endpoint
        response = client.get(f"/receptions/{mock_reception_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_reception_data["id"]

        # Verify service function was called correctly
        mock_get_reception.assert_called_once_with(ANY, mock_reception_data["id"])

    @patch('app.routers.reception.reception_service.get_reception')
    def test_get_reception_not_found(self, mock_get_reception):
        # Configure mock
        mock_get_reception.return_value = None

        # Test the endpoint
        response = client.get("/receptions/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.reception.reception_service.update_reception')
    def test_update_reception_success(self, mock_update_reception):
        # Configure mock
        updated_reception = mock_reception_model
        updated_reception.quantite = 75
        updated_reception.fournisseur = "Fournisseur Test Updated"
        mock_update_reception.return_value = updated_reception

        # Test the endpoint
        response = client.put(
            f"/receptions/{mock_reception_data['id']}",
            json={
                "article_id": "A12345",
                "quantite": 75,
                "fournisseur": "Fournisseur Test Updated",
                "date_reception": current_datetime.isoformat(),
                "emplacement_id": "E12345"
            }
        )

        # Verify response
        assert response.status_code == 200
        assert response.json()["quantite"] == 75
        assert response.json()["fournisseur"] == "Fournisseur Test Updated"

        # Verify service function was called correctly
        mock_update_reception.assert_called_once()

    @patch('app.routers.reception.reception_service.update_reception')
    def test_update_reception_not_found(self, mock_update_reception):
        # Configure mock
        mock_update_reception.return_value = None

        # Test the endpoint
        response = client.put(
            "/receptions/nonexistent",
            json={
                "article_id": "A12345",
                "quantite": 75,
                "fournisseur": "Fournisseur Test Updated",
                "date_reception": current_datetime.isoformat(),
                "emplacement_id": "E12345"
            }
        )

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.reception.reception_service.delete_reception')
    def test_delete_reception_success(self, mock_delete_reception):
        # Configure mock
        mock_delete_reception.return_value = mock_reception_model

        # Test the endpoint
        response = client.delete(f"/receptions/{mock_reception_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_reception_data["id"]

        # Verify service function was called correctly
        mock_delete_reception.assert_called_once_with(ANY, mock_reception_data["id"])

    @patch('app.routers.reception.reception_service.delete_reception')
    def test_delete_reception_not_found(self, mock_delete_reception):
        # Configure mock
        mock_delete_reception.return_value = None

        # Test the endpoint
        response = client.delete("/receptions/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]