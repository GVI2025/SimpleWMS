from fastapi.testclient import TestClient
from unittest.mock import patch, ANY
from datetime import datetime

from app.main import app
from app.schemas.reservation import ReservationCreate, ReservationUpdate
from app.services.salle import SalleCreate, SalleUpdate
from app.models import Reservation as ReservationModel, Salle as SalleModel


client = TestClient(app)

mock_salle_data = {
    "id": "12345",
    "nom": "Test Salle",
    "capacité": 100,
    "localisation": "Test Localisation",
    "disponible": True,
}

mock_salle_client = SalleModel(
    id="12345",
    nom="Test Salle",
    capacité=100,
    localisation="Test Localisation",
    disponible=True,
)

mock_salle_create = SalleCreate(
    nom="Test Salle",
    capacité=100,
    localisation="Test Localisation",
    disponible=True,
)

mock_salle_update = SalleUpdate(
    nom="Updated Salle",
    capacité=150,
    localisation="Updated Localisation",
    disponible=False,
)

mock_reservation_data = {
    "id": "123456",
    "salle_id": "12345",
    "utilisateur": "albert",
    "date": "2023-10-01",
    "heure": "10:00:00",
    "commentaire": "Ceci est un commentaire",
}

mock_reservation_create = ReservationCreate(
    salle_id="12345",
    utilisateur="albert",
    date="2023-10-01",
    heure="10:00:00",
    commentaire="Ceci est un commentaire",
)

mock_update_reservation = ReservationUpdate(
    salle_id="12345",
    utilisateur="albert_updated",
    date="2023-10-01",
    heure="10:00:00",
    commentaire="Ceci est un commentaire mis à jour",
)


class TestIntegration:

    @patch("app.services.salle.create_salle")
    def test_create_salle(self, mock_create_salle):
        mock_create_salle.return_value = mock_salle_data
        response = client.post("/salles/", json=mock_salle_create.model_dump())
        assert response.status_code == 200
        assert response.json() == mock_salle_data

    @patch("app.services.reservation.create_reservation")
    def test_create_reservation(self, mock_create_reservation):
        mock_create_reservation.return_value = mock_reservation_data

        response = client.post("/reservations/", json={
            "id": "123456",
            "salle_id": "12345",
            "utilisateur": "albert",
            "date": "2023-10-01",
            "heure": "10:00:00",
            "commentaire": "Ceci est un commentaire",
        })
        assert response.status_code == 200
        assert response.json() == mock_reservation_data


    @patch("app.services.salle.list_salles")
    def test_list_salle(self, mock_get_all_salles):
        mock_get_all_salles.return_value = [mock_salle_data]
        response = client.get("/salles/")
        assert response.status_code == 200
        assert response.json() == [mock_salle_data]

    @patch("app.services.reservation.get_reservation")
    def test_get_reservation(self, mock_get_reservation):
        mock_get_reservation.return_value = [mock_reservation_data]

        response = client.get("/reservations/")
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0] == mock_reservation_data

    @patch("app.services.salle.get_salle")
    def test_get_salle(self, mock_get_salle):
        mock_get_salle.return_value = mock_salle_data

        response = client.get(f"/salles/{mock_salle_data['id']}")
        assert response.status_code == 200
        assert response.json() == mock_salle_data

    @patch("app.services.reservation.get_reservations_by_salle")
    def test_get_reservations_by_salle(self, mock_get_reservations_by_salle):
        mock_get_reservations_by_salle.return_value = [mock_reservation_data]

        response = client.get("/reservations/salle_001")
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0] == mock_reservation_data

    @patch("app.services.salle.update_salle")
    def test_update_salle(self, mock_update_salle):
        updated_salle = mock_salle_client
        updated_salle.nom = mock_salle_update.nom
        updated_salle.capacité = mock_salle_update.capacité
        updated_salle.localisation = mock_salle_update.localisation
        updated_salle.disponible = mock_salle_update.disponible
        
        mock_update_salle.return_value = updated_salle

        # Test the update endpoint
        response = client.put(
            "/salles/test_id", 
            json={
                "nom": "updated salle",
                "capacité": 150,
                "localisation": "updated localisation",
                "disponible": False
            }
        )

        assert response.status_code == 200
        assert response.json()["nom"] == mock_salle_update.nom
        assert response.json()["capacité"] == mock_salle_update.capacité
        assert response.json()["localisation"] == mock_salle_update.localisation

    @patch("app.services.salle.delete_salle")
    def test_delete_salle(self, mock_delete_salle):

        response = client.delete(f"/reservations/{mock_reservation_data['id']}")
        assert response.status_code == 200
        assert response.json() == {"message": "Réservation supprimée avec succès"}

    @patch("app.services.salle.delete_salle")
    def test_delete_salle(self, mock_delete_salle):
        response = client.delete(f"/salles/{mock_salle_data['id']}")
        assert response.status_code == 200

    @patch("app.services.salle.list_salles")
    def test_list_salles_empty(self, mock_list_salles):
        mock_list_salles.return_value = []
        response = client.get("/salles/")
        assert response.status_code == 200
        assert response.json() == []

    @patch("app.services.reservation.get_reservation")
    def test_get_reservation_empty(self, mock_get_reservation):
        mock_get_reservation.return_value = []

        response = client.get("/reservations/")
        assert response.status_code == 200
        assert response.json() == []
