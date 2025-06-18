from fastapi.testclient import TestClient
from unittest.mock import patch, ANY
from datetime import datetime

from app.main import app
from app.schemas.reservation import ReservationCreate, ReservationUpdate
from app.models import Reservation as ReservationModel  

client = TestClient(app)


mock_reservation_data = {
    "id": "12345",
    "salle_id": "salle_001",
    "utilisateur": "albert",
    "date": "2023-10-01",
    "heure": "10:00:00",
}

mock_reservation_create = ReservationCreate(
    salle_id="salle_001",
    utilisateur="albert",
    date="2023-10-01",
    heure="10:00:00",
)

mock_reservation_update = ReservationUpdate(
    salle_id="salle_001",
    utilisateur="albert_updated",
    date="2023-10-01",
    heure="10:00:00",
)

mock_reservation_model = ReservationModel(
    id="12345",
    salle_id="salle_001",
    utilisateur="albert",
    date="2023-10-01",
    heure="10:00:00",
)

mock_reservation_list = [
    ReservationModel(
        id="12345",
        salle_id="salle_001",
        utilisateur="albert",
        date="2023-10-01",
        heure="10:00:00",
    ),
    ReservationModel(
        id="67890",
        salle_id="salle_002",
        utilisateur="bob",
        date="2023-10-01",
        heure="10:00:00",
    ),
]

@patch("app.services.reservation.create_reservation")
def test_create_reservation(mock_create_reservation):
    mock_create_reservation.return_value = mock_reservation_model

    response = client.post("/reservations/", json=mock_reservation_create.dict())
    assert response.status_code == 201
    assert response.json() == mock_reservation_data

@patch("app.services.reservation.get_reservation")
def test_get_reservation(mock_get_reservation):
    mock_get_reservation.return_value = mock_reservation_model

    response = client.get("/reservations/12345")
    assert response.status_code == 200
    assert response.json() == mock_reservation_data

@patch("app.services.reservation.update_reservation")
def test_update_reservation(mock_update_reservation):
    mock_update_reservation.return_value = mock_reservation_model

    response = client.put("/reservations/12345", json=mock_reservation_update.dict())
    assert response.status_code == 200
    assert response.json() == mock_reservation_data

@patch("app.services.reservation.delete_reservation")
def test_delete_reservation(mock_delete_reservation):
    mock_delete_reservation.return_value = mock_reservation_model

    response = client.delete("/reservations/12345")
    assert response.status_code == 200
    assert response.json() == mock_reservation_data






    

