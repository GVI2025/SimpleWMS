from fastapi.testclient import TestClient
from unittest.mock import patch, ANY

from app.main import app
from app.schemas.agent import AgentCreate, AgentUpdate
from app.models import Agent as AgentModel

client = TestClient(app)

# Mock agent data
mock_agent_data = {
    "id": "12345",
    "nom": "Dupont",
    "email": "jean.dupont@example.com",
    "actif": True
}

mock_agent_create = AgentCreate(
    nom="Dupont",
    email="jean.dupont@example.com"
)

mock_agent_update = AgentUpdate(
    nom="Dupont-Updated",
    email="jean.dupont@example.com",
    actif=False
)

mock_agent_model = AgentModel(
    id="12345",
    nom="Dupont",
    email="jean.dupont@example.com",
    actif=True
)

mock_agent_list = [
    AgentModel(
        id="12345",
        nom="Dupont",
        email="jean.dupont@example.com",
        actif=True
    ),
    AgentModel(
        id="67890",
        nom="Martin",
        email="sophie.martin@example.com",
        actif=True
    )
]


class TestAgentRouter:
    @patch('app.routers.agent.agent_service.list_agents')
    def test_list_agents(self, mock_list_agents):
        # Configure mock
        mock_list_agents.return_value = mock_agent_list

        # Test the endpoint
        response = client.get("/agents/")

        # Verify response
        assert response.status_code == 200
        assert len(response.json()) == 2

        # Verify that service function was called with correct parameters
        mock_list_agents.assert_called_once()
        # Using correct way to access call parameters
        _, kwargs = mock_list_agents.call_args

    @patch('app.routers.agent.agent_service.get_agent_by_email')
    @patch('app.routers.agent.agent_service.create_agent')
    def test_create_agent_success(self, mock_create_agent, mock_get_by_email):
        # Configure mocks
        mock_get_by_email.return_value = None
        mock_create_agent.return_value = mock_agent_model

        # Test the endpoint
        response = client.post("/agents/", json={
            "nom": "Dupont",
            "email": "jean.dupont@example.com"
        })

        # Verify response
        assert response.status_code == 200
        assert response.json()["email"] == mock_agent_data["email"]

        # Verify service functions were called correctly
        mock_get_by_email.assert_called_once_with(ANY, mock_agent_data["email"])
        mock_create_agent.assert_called_once()

    @patch('app.routers.agent.agent_service.get_agent_by_email')
    def test_create_agent_duplicate_email(self, mock_get_by_email):
        # Configure mock to simulate duplicate email
        mock_get_by_email.return_value = mock_agent_model

        # Test the endpoint
        response = client.post("/agents/", json={
            "nom": "Dupont",
            "email": "jean.dupont@example.com"
        })

        # Verify response
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    @patch('app.routers.agent.agent_service.get_agent')
    def test_get_agent_success(self, mock_get_agent):
        # Configure mock
        mock_get_agent.return_value = mock_agent_model

        # Test the endpoint
        response = client.get(f"/agents/{mock_agent_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_agent_data["id"]

        # Verify service function was called correctly
        mock_get_agent.assert_called_once_with(ANY, mock_agent_data["id"])

    @patch('app.routers.agent.agent_service.get_agent')
    def test_get_agent_not_found(self, mock_get_agent):
        # Configure mock
        mock_get_agent.return_value = None

        # Test the endpoint
        response = client.get("/agents/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.agent.agent_service.update_agent')
    def test_update_agent_success(self, mock_update_agent):
        # Configure mock
        updated_agent = mock_agent_model
        updated_agent.nom = "Dupont-Updated"
        updated_agent.actif = False
        mock_update_agent.return_value = updated_agent

        # Test the endpoint
        response = client.put(
            f"/agents/{mock_agent_data['id']}",
            json={
                "nom": "Dupont-Updated",
                "email": "jean.dupont@example.com",
                "actif": False
            }
        )

        # Verify response
        assert response.status_code == 200
        assert response.json()["nom"] == "Dupont-Updated"
        assert response.json()["actif"] is False

        # Verify service function was called correctly
        mock_update_agent.assert_called_once()

    @patch('app.routers.agent.agent_service.update_agent')
    def test_update_agent_not_found(self, mock_update_agent):
        # Configure mock
        mock_update_agent.return_value = None

        # Test the endpoint
        response = client.put(
            "/agents/nonexistent",
            json={
                "nom": "Dupont-Updated",
                "email": "jean.dupont@example.com",
                "actif": False
            }
        )

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.agent.agent_service.delete_agent')
    def test_delete_agent_success(self, mock_delete_agent):
        # Configure mock
        mock_delete_agent.return_value = mock_agent_model

        # Test the endpoint
        response = client.delete(f"/agents/{mock_agent_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_agent_data["id"]

        # Verify service function was called correctly
        mock_delete_agent.assert_called_once_with(ANY, mock_agent_data["id"])

    @patch('app.routers.agent.agent_service.delete_agent')
    def test_delete_agent_not_found(self, mock_delete_agent):
        # Configure mock
        mock_delete_agent.return_value = None

        # Test the endpoint
        response = client.delete("/agents/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]