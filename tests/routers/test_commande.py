from fastapi.testclient import TestClient
from unittest.mock import patch, ANY

from app.main import app
from app.schemas.commande import CommandeCreate, CommandeUpdate, EtatCommande, LigneCommandeCreate
from app.models import Commande as CommandeModel, LigneCommande as LigneModel

client = TestClient(app)

# Mock commande data
mock_ligne = {
    "id": "L12345",
    "article_id": "A12345",
    "quantite": 5
}

mock_commande_data = {
    "id": "C12345",
    "reference": "CMD001",
    "etat": EtatCommande.BROUILLON,
    "lignes": [mock_ligne]
}

mock_ligne_create = LigneCommandeCreate(
    article_id="A12345",
    quantite=5
)

mock_commande_create = CommandeCreate(
    reference="CMD001",
    etat=EtatCommande.BROUILLON,
    lignes=[mock_ligne_create]
)

mock_commande_update = CommandeUpdate(
    reference="CMD001",
    etat=EtatCommande.RESERVEE
)

mock_ligne_model = LigneModel(
    id="L12345",
    commande_id="C12345",
    article_id="A12345",
    quantite=5
)

mock_commande_model = CommandeModel(
    id="C12345",
    reference="CMD001",
    etat=EtatCommande.BROUILLON,
    lignes=[mock_ligne_model]
)

mock_commande_list = [
    CommandeModel(
        id="C12345",
        reference="CMD001",
        etat=EtatCommande.BROUILLON,
        lignes=[mock_ligne_model]
    ),
    CommandeModel(
        id="C67890",
        reference="CMD002",
        etat=EtatCommande.PREPAREE,
        lignes=[]
    )
]


class TestCommandeRouter:
    @patch('app.routers.commande.commande_service.list_commandes')
    def test_list_commandes(self, mock_list_commandes):
        # Configure mock
        mock_list_commandes.return_value = mock_commande_list

        # Test the endpoint
        response = client.get("/commandes/")

        # Verify response
        assert response.status_code == 200
        assert len(response.json()) == 2

        # Verify service function was called
        mock_list_commandes.assert_called_once()

    @patch('app.routers.commande.commande_service.get_commande_by_reference')
    @patch('app.routers.commande.commande_service.create_commande')
    def test_create_commande_success(self, mock_create_commande, mock_get_by_reference):
        # Configure mocks
        mock_get_by_reference.return_value = None
        mock_create_commande.return_value = mock_commande_model

        # Test the endpoint
        response = client.post("/commandes/", json={
            "reference": "CMD001",
            "etat": "Brouillon",
            "lignes": [
                {
                    "article_id": "A12345",
                    "quantite": 5
                }
            ]
        })

        # Verify response
        assert response.status_code == 200
        assert response.json()["reference"] == "CMD001"

        # Verify service functions were called correctly
        mock_get_by_reference.assert_called_once_with(ANY, "CMD001")
        mock_create_commande.assert_called_once()

    @patch('app.routers.commande.commande_service.get_commande_by_reference')
    def test_create_commande_duplicate_reference(self, mock_get_by_reference):
        # Configure mock to simulate duplicate reference
        mock_get_by_reference.return_value = mock_commande_model

        # Test the endpoint
        response = client.post("/commandes/", json={
            "reference": "CMD001",
            "etat": "Brouillon",
            "lignes": [
                {
                    "article_id": "A12345",
                    "quantite": 5
                }
            ]
        })

        # Verify response
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    @patch('app.routers.commande.commande_service.get_commande')
    def test_get_commande_success(self, mock_get_commande):
        # Configure mock
        mock_get_commande.return_value = mock_commande_model

        # Test the endpoint
        response = client.get(f"/commandes/{mock_commande_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_commande_data["id"]

        # Verify service function was called correctly
        mock_get_commande.assert_called_once_with(ANY, mock_commande_data["id"])

    @patch('app.routers.commande.commande_service.get_commande')
    def test_get_commande_not_found(self, mock_get_commande):
        # Configure mock
        mock_get_commande.return_value = None

        # Test the endpoint
        response = client.get("/commandes/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.commande.commande_service.update_commande')
    def test_update_commande_success(self, mock_update_commande):
        # Configure mock
        updated_commande = mock_commande_model
        updated_commande.etat = EtatCommande.RESERVEE
        mock_update_commande.return_value = updated_commande

        # Test the endpoint
        response = client.put(
            f"/commandes/{mock_commande_data['id']}",
            json={
                "reference": "CMD001",
                "etat": "Réservée"
            }
        )

        # Verify response
        assert response.status_code == 200
        assert response.json()["etat"] == "Réservée"

        # Verify service function was called correctly
        mock_update_commande.assert_called_once()

    @patch('app.routers.commande.commande_service.update_commande')
    def test_update_commande_not_found(self, mock_update_commande):
        # Configure mock
        mock_update_commande.return_value = None

        # Test the endpoint
        response = client.put(
            "/commandes/nonexistent",
            json={
                "reference": "CMD001",
                "etat": "Réservée"
            }
        )

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.commande.commande_service.delete_commande')
    def test_delete_commande_success(self, mock_delete_commande):
        # Configure mock
        mock_delete_commande.return_value = mock_commande_model

        # Test the endpoint
        response = client.delete(f"/commandes/{mock_commande_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_commande_data["id"]

        # Verify service function was called correctly
        mock_delete_commande.assert_called_once_with(ANY, mock_commande_data["id"])

    @patch('app.routers.commande.commande_service.delete_commande')
    def test_delete_commande_not_found(self, mock_delete_commande):
        # Configure mock
        mock_delete_commande.return_value = None

        # Test the endpoint
        response = client.delete("/commandes/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    def test_list_commandes_by_designation(client, db_session, article_factory, commande_factory, ligne_commande_factory):
        # Crée deux articles
        perceuse = article_factory(designation="Perceuse Bosch")
        visseuse = article_factory(designation="Visseuse Makita")
        # Crée deux commandes
        commande1 = commande_factory()
        commande2 = commande_factory()
        # Ajoute une ligne de commande avec la perceuse à la commande1
        ligne_commande_factory(commande=commande1, article=perceuse)
        # Ajoute une ligne de commande avec la visseuse à la commande2
        ligne_commande_factory(commande=commande2, article=visseuse)
        db_session.commit()

        # Recherche "perceuse"
        response = client.get("/commandes?designation=perceuse")
        assert response.status_code == 200
        results = response.json()
        assert len(results) == 1
        assert any("perceuse" in ligne["article"]["designation"].lower() for commande in results for ligne in commande["lignes"])