from fastapi.testclient import TestClient
from unittest.mock import patch, ANY
from datetime import datetime

from app.main import app
from app.schemas.mission import MissionCreate, MissionUpdate, TypeMission, EtatMission
from app.models import Mission as MissionModel

client = TestClient(app)

# Mock mission data
current_datetime = datetime.now()

mock_mission_data = {
    "id": "12345",
    "type": TypeMission.DEPLACEMENT,
    "etat": EtatMission.A_FAIRE,
    "article_id": "A12345",
    "source_id": "E12345",
    "destination_id": "E67890",
    "quantite": 10,
    "agent_id": "AGT001",
    "date_creation": current_datetime,
    "date_execution": None
}

mock_mission_create = MissionCreate(
    type=TypeMission.DEPLACEMENT,
    etat=EtatMission.A_FAIRE,
    article_id="A12345",
    source_id="E12345",
    destination_id="E67890",
    quantite=10,
    agent_id="AGT001",
    date_creation=current_datetime,
    date_execution=None
)

mock_mission_update = MissionUpdate(
    type=TypeMission.DEPLACEMENT,
    etat=EtatMission.EN_COURS,
    article_id="A12345",
    source_id="E12345",
    destination_id="E67890",
    quantite=10,
    agent_id="AGT001",
    date_creation=current_datetime,
    date_execution=current_datetime
)

mock_mission_model = MissionModel(
    id="12345",
    type=TypeMission.DEPLACEMENT,
    etat=EtatMission.A_FAIRE,
    article_id="A12345",
    source_id="E12345",
    destination_id="E67890",
    quantite=10,
    agent_id="AGT001",
    date_creation=current_datetime,
    date_execution=None
)

mock_mission_list = [
    MissionModel(
        id="12345",
        type=TypeMission.DEPLACEMENT,
        etat=EtatMission.A_FAIRE,
        article_id="A12345",
        source_id="E12345",
        destination_id="E67890",
        quantite=10,
        agent_id="AGT001",
        date_creation=current_datetime,
        date_execution=None
    ),
    MissionModel(
        id="67890",
        type=TypeMission.INVENTAIRE,
        etat=EtatMission.TERMINE,
        article_id="A67890",
        source_id="E67890",
        destination_id=None,
        quantite=25,
        agent_id="AGT002",
        date_creation=current_datetime,
        date_execution=current_datetime
    )
]


class TestMissionRouter:
    @patch('app.routers.mission.mission_service.list_missions')
    def test_list_missions(self, mock_list_missions):
        # Configure mock
        mock_list_missions.return_value = mock_mission_list

        # Test the endpoint
        response = client.get("/missions/")

        # Verify response
        assert response.status_code == 200
        assert len(response.json()) == 2

        # Verify service function was called
        mock_list_missions.assert_called_once()

    @patch('app.routers.mission.mission_service.create_mission')
    def test_create_mission_success(self, mock_create_mission):
        # Configure mock
        mock_create_mission.return_value = mock_mission_model

        # Test the endpoint
        response = client.post("/missions/", json={
            "type": "Déplacement",
            "etat": "À faire",
            "article_id": "A12345",
            "source_id": "E12345",
            "destination_id": "E67890",
            "quantite": 10,
            "agent_id": "AGT001",
            "date_creation": current_datetime.isoformat(),
            "date_execution": None
        })

        # Verify response
        assert response.status_code == 200
        assert response.json()["article_id"] == "A12345"
        assert response.json()["etat"] == "À faire"

        # Verify service function was called correctly
        mock_create_mission.assert_called_once()

    @patch('app.routers.mission.mission_service.get_mission')
    def test_get_mission_success(self, mock_get_mission):
        # Configure mock
        mock_get_mission.return_value = mock_mission_model

        # Test the endpoint
        response = client.get(f"/missions/{mock_mission_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_mission_data["id"]

        # Verify service function was called correctly
        mock_get_mission.assert_called_once_with(ANY, mock_mission_data["id"])

    @patch('app.routers.mission.mission_service.get_mission')
    def test_get_mission_not_found(self, mock_get_mission):
        # Configure mock
        mock_get_mission.return_value = None

        # Test the endpoint
        response = client.get("/missions/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.mission.mission_service.update_mission')
    def test_update_mission_success(self, mock_update_mission):
        # Configure mock
        updated_mission = mock_mission_model
        updated_mission.etat = EtatMission.EN_COURS
        updated_mission.date_execution = current_datetime
        mock_update_mission.return_value = updated_mission

        # Test the endpoint
        response = client.put(
            f"/missions/{mock_mission_data['id']}",
            json={
                "type": "Déplacement",
                "etat": "En cours",
                "article_id": "A12345",
                "source_id": "E12345",
                "destination_id": "E67890",
                "quantite": 10,
                "agent_id": "AGT001",
                "date_creation": current_datetime.isoformat(),
                "date_execution": current_datetime.isoformat()
            }
        )

        # Verify response
        assert response.status_code == 200
        assert response.json()["etat"] == "En cours"
        assert response.json()["date_execution"] is not None

        # Verify service function was called correctly
        mock_update_mission.assert_called_once()

    @patch('app.routers.mission.mission_service.update_mission')
    def test_update_mission_not_found(self, mock_update_mission):
        # Configure mock
        mock_update_mission.return_value = None

        # Test the endpoint
        response = client.put(
            "/missions/nonexistent",
            json={
                "type": "Déplacement",
                "etat": "En cours",
                "article_id": "A12345",
                "source_id": "E12345",
                "destination_id": "E67890",
                "quantite": 10,
                "agent_id": "AGT001",
                "date_creation": current_datetime.isoformat(),
                "date_execution": current_datetime.isoformat()
            }
        )

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.mission.mission_service.delete_mission')
    def test_delete_mission_success(self, mock_delete_mission):
        # Configure mock
        mock_delete_mission.return_value = mock_mission_model

        # Test the endpoint
        response = client.delete(f"/missions/{mock_mission_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_mission_data["id"]

        # Verify service function was called correctly
        mock_delete_mission.assert_called_once_with(ANY, mock_mission_data["id"])

    @patch('app.routers.mission.mission_service.delete_mission')
    def test_delete_mission_not_found(self, mock_delete_mission):
        # Configure mock
        mock_delete_mission.return_value = None

        # Test the endpoint
        response = client.delete("/missions/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]