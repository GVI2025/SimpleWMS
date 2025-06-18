
from app.database.database import SessionLocal
from app.models.reservation import Reservation
from app.models.salle import Salle

from datetime import datetime, date
from sqlalchemy.exc import IntegrityError

def seed():
    db = SessionLocal()
    try:
        # Nettoyage de la base (dans l'ordre inverse des dépendances)
        db.query(Salle).delete()
        db.query(Reservation).delete()
        db.commit()

        # === SALLES ===
        salles = [
            Salle(id="salle1", nom="Salle A", capacite=10, description="Salle de réunion A"),
            Salle(id="salle2", nom="Salle B", capacite=20, description="Salle de réunion B"),
            Salle(id="salle3", nom="Salle C", capacite=30, description="Salle de réunion C"),
            Salle(id="salle4", nom="Salle D", capacite=15, description="Salle de réunion D"),
        ]

        # === RESERVATIONS ===
        reservations = [
            Reservation(id="reservation1", salle_id="salle1", date=date(2023, 10, 1), heure_debut=datetime(2023, 10, 1, 9, 0), heure_fin=datetime(2023, 10, 1, 10, 0), description="Réunion de projet"),
            Reservation(id="reservation2", salle_id="salle2", date=date(2023, 10, 2), heure_debut=datetime(2023, 10, 2, 11, 0), heure_fin=datetime(2023, 10, 2, 12, 0), description="Formation interne"),
            Reservation(id="reservation3", salle_id="salle3", date=date(2023, 10, 3), heure_debut=datetime(2023, 10, 3, 14, 0), heure_fin=datetime(2023, 10, 3, 15, 0), description="Réunion d'équipe")
        ]

        # Ajout global
        db.add_all(salles + reservations)
        db.commit()
        print("Données de test insérées avec succès.")

    except IntegrityError as e:
        db.rollback()
        print("Erreur d'intégrité :", e)
    finally:
        db.close()

if __name__ == "__main__":
    seed()