from fastapi.testclient import TestClient
from unittest.mock import patch, ANY

from app.main import app
from app.schemas.emplacement import EmplacementCreate, EmplacementUpdate
from app.models import Emplacement as EmplacementModel

client = TestClient(app)

# Données simulées
mock_emplacement_data = {
    "id": "e1",
    "code": "Z-A",
    "nom": "Zone A",
    "description": "Zone de stockage A",
    "actif": True
}

mock_emplacement_create = EmplacementCreate(
    code="Z-A",
    nom="Zone A",
    description="Zone de stockage A"
)

mock_emplacement_update = EmplacementUpdate(
    code="Z-A",
    nom="Zone A modifiée",
    description="Nouvelle description",
    actif=False
)

mock_emplacement_model = EmplacementModel(
    id="e1",
    code="Z-A",
    nom="Zone A",
    description="Zone de stockage A",
    actif=True
)

mock_emplacement_list = [
    EmplacementModel(
        id="e1",
        code="Z-A",
        nom="Zone A",
        description="Zone de stockage A",
        actif=True
    ),
    EmplacementModel(
        id="e2",
        code="Z-B",
        nom="Zone B",
        description="Zone de stockage B",
        actif=True
    )
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

        response = client.post("/emplacements/", json={
            "code": "Z-A",
            "nom": "Zone A",
            "description": "Zone de stockage A"
        })

        assert response.status_code == 200
        assert response.json()["code"] == mock_emplacement_data["code"]

        mock_get_by_code.assert_called_once_with(ANY, mock_emplacement_data["code"])
        mock_create_emplacement.assert_called_once()

    @patch('app.routers.emplacement.emplacement_service.get_emplacement_by_code')
    def test_create_emplacement_duplicate_code(self, mock_get_by_code):
        mock_get_by_code.return_value = mock_emplacement_model

        response = client.post("/emplacements/", json={
            "code": "Z-A",
            "nom": "Zone A",
            "description": "Zone de stockage A"
        })

        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_success(self, mock_get_emplacement):
        mock_get_emplacement.return_value = mock_emplacement_model

        response = client.get("/emplacements/e1")

        assert response.status_code == 200
        assert response.json()["id"] == mock_emplacement_data["id"]
        mock_get_emplacement.assert_called_once_with(ANY, mock_emplacement_data["id"])

    @patch('app.routers.emplacement.emplacement_service.get_emplacement')
    def test_get_emplacement_not_found(self, mock_get_emplacement):
        mock_get_emplacement.return_value = None

        response = client.get("/emplacements/inexistant")

        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_success(self, mock_update_emplacement):
        updated = mock_emplacement_model
        updated.nom = "Zone A modifiée"
        updated.actif = False
        mock_update_emplacement.return_value = updated

        response = client.put("/emplacements/e1", json={
            "code": "Z-A",
            "nom": "Zone A modifiée",
            "description": "Nouvelle description",
            "actif": False
        })

        assert response.status_code == 200
        assert response.json()["nom"] == "Zone A modifiée"
        assert response.json()["actif"] is False

    @patch('app.routers.emplacement.emplacement_service.update_emplacement')
    def test_update_emplacement_not_found(self, mock_update_emplacement):
        mock_update_emplacement.return_value = None

        response = client.put("/emplacements/inexistant", json={
            "code": "Z-A",
            "nom": "Zone A modifiée",
            "description": "Nouvelle description",
            "actif": False
        })

        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_success(self, mock_delete_emplacement):
        mock_delete_emplacement.return_value = mock_emplacement_model

        response = client.delete("/emplacements/e1")

        assert response.status_code == 200
        assert response.json()["id"] == mock_emplacement_data["id"]
        mock_delete_emplacement.assert_called_once_with(ANY, mock_emplacement_data["id"])

    @patch('app.routers.emplacement.emplacement_service.delete_emplacement')
    def test_delete_emplacement_not_found(self, mock_delete_emplacement):
        mock_delete_emplacement.return_value = None

        response = client.delete("/emplacements/inexistant")

        assert response.status_code == 404
        assert "not found" in response.json()["detail"]
