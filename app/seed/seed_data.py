
from datetime import datetime, date

from sqlalchemy.exc import IntegrityError
import uuid

from app.database.database import SessionLocal
from app.models.agent import Agent
from app.models.article import Article
from app.models.commande import Commande, LigneCommande
from app.models.emplacement import Emplacement
from app.models.implantation import Implantation
from app.models.mission import Mission
from app.models.reception import Reception


def init_seed_data():
    db = SessionLocal()
    try:
        # Nettoyage de la base (dans l'ordre inverse des dépendances)
        db.query(Mission).delete()
        db.query(Reception).delete()
        db.query(Implantation).delete()
        db.query(LigneCommande).delete()
        db.query(Commande).delete()
        db.query(Agent).delete()
        db.query(Emplacement).delete()
        db.query(Article).delete()
        db.commit()

        # === ARTICLES ===
        articles = [
            Article(
                id='10d55c46-9840-43f0-8dc5-23f8453b16d6',
                sku='ART1000',
                designation='Article 0',
                categorie='PRODUIT',
                poids_kg=1.95,
                volume_m3=0.111,
                date_peremption=None,
            ),
            Article(
                id='da3d5688-0748-4461-ab27-5932b707d18f',
                sku='ART1001',
                designation='Article 1',
                categorie='CONSOMMABLE',
                poids_kg=6.99,
                volume_m3=0.791,
                date_peremption=None,
            ),
            Article(
                id='620d48b8-48ac-4353-9fa6-be268263c56c',
                sku='ART1002',
                designation='Article 2',
                categorie='PRODUIT',
                poids_kg=5.56,
                volume_m3=0.509,
                date_peremption=date(2024, 11, 6)
            ),
            Article(
                id='5382f5bb-3b3a-4c11-886b-c3264eb441c5',
                sku='ART1003',
                designation='Article 3',
                categorie='PIECE',
                poids_kg=8.39,
                volume_m3=0.911,
                date_peremption=None,
            ),
            Article(
                id='7a855ef8-ed39-4c8b-9cfa-6696e48a1aa7',
                sku='ART1004',
                designation='Article 4',
                categorie='CONSOMMABLE',
                poids_kg=0.12,
                volume_m3=0.417,
                date_peremption=date(2024, 8, 20),
            ),
            Article(
                id='05a602fc-ec0c-43d7-a0fb-f2f1824e9d69',
                sku='ART1005',
                designation='Article 5',
                categorie='PRODUIT',
                poids_kg=1.82,
                volume_m3=0.814,
                date_peremption=date(2025, 2, 21),
            ),
            Article(
                id='774e9f91-957c-48f1-8e40-810f6b161cf3',
                sku='ART1006',
                designation='Article 6',
                categorie='PRODUIT',
                poids_kg=1.38,
                volume_m3=0.505,
                date_peremption=date(2024, 10, 29),
            ),
            Article(
                id='6d5c4080-8b1a-4a37-9c32-7e9d1bfe0d40',
                sku='ART1007',
                designation='Article 7',
                categorie='PIECE',
                poids_kg=1.32,
                volume_m3=0.569,
                date_peremption=date(2025, 10, 5),
            ),
            Article(
                id='1f5b5fe1-7048-479a-9027-56dfbfd796e2',
                sku='ART1008',
                designation='Article 8',
                categorie='CONSOMMABLE',
                poids_kg=5.56,
                volume_m3=0.081,
                date_peremption=None,
            ),
            Article(
                id='395b92df-ca7a-46b4-b3e7-9e3513248c60',
                sku='ART1009',
                designation='Article 9',
                categorie='PIECE',
                poids_kg=9.82,
                volume_m3=0.151,
                date_peremption=None,
            ),
            Article(
                id='e0e1ba1c-5e74-4443-896f-d97173e6d75b',
                sku='ART1010',
                designation='Article 10',
                categorie='CONSOMMABLE',
                poids_kg=0.35,
                volume_m3=0.049,
                date_peremption=date(2024, 7, 16),
            ),
            Article(
                id='168a6854-579d-4838-a9c4-3c5679bc677a',
                sku='ART1011',
                designation='Article 11',
                categorie='PRODUIT',
                poids_kg=4.67,
                volume_m3=0.328,
                date_peremption=date(2024, 10, 5),
            ),
            Article(
                id='1a4649e4-e6d6-4737-8aa9-c614f558a39f',
                sku='ART1012',
                designation='Article 12',
                categorie='CONSOMMABLE',
                poids_kg=5.14,
                volume_m3=0.044,
                date_peremption=None,
            ),
            Article(
                id='cef516c1-6599-47c3-a189-7a2fc515037f',
                sku='ART1013',
                designation='Article 13',
                categorie='CONSOMMABLE',
                poids_kg=6.2,
                volume_m3=0.572,
                date_peremption=date(2025, 11, 17),
            ),
            Article(
                id='a9a90b6d-b4cc-4e68-b222-6578f3ae3502',
                sku='ART1014',
                designation='Article 14',
                categorie='PIECE',
                poids_kg=7.33,
                volume_m3=0.51,
                date_peremption=date(2024, 8, 12),
            ),
            Article(
                id='6c572a1c-bc0a-4bd5-ae62-460600c6ed23',
                sku='ART1015',
                designation='Article 15',
                categorie='PRODUIT',
                poids_kg=3.76,
                volume_m3=0.97,
                date_peremption=None,
            ),
            Article(
                id='ce79cf87-384b-4ad3-86f9-6808ace2d67c',
                sku='ART1016',
                designation='Article 16',
                categorie='CONSOMMABLE',
                poids_kg=6.66,
                volume_m3=0.26,
                date_peremption=None,
            ),
            Article(
                id='4d0b10ae-6a0b-4c96-9f54-6b511952f5d6',
                sku='ART1017',
                designation='Article 17',
                categorie='PRODUIT',
                poids_kg=9.53,
                volume_m3=0.76,
                date_peremption=date(2024, 5, 19),
            ),
            Article(
                id='fbdc7d09-7169-42e1-905f-fcfbacb91fc3',
                sku='ART1018',
                designation='Article 18',
                categorie='CONSOMMABLE',
                poids_kg=5.24,
                volume_m3=0.387,
                date_peremption=None,
            ),
            Article(
                id='3bc80159-d354-43d9-9085-0bb1a54d6856',
                sku='ART1019',
                designation='Article 19',
                categorie='PRODUIT',
                poids_kg=5.28,
                volume_m3=0.845,
                date_peremption=None,
            ),
        ]

        # === AGENTS ===
        agents = [
            Agent(
                id='17ec87fd-6f24-4e2c-a6b6-7928025a94b3',
                nom='Agent 0',
                email='agent0@example.com',
                actif=True,
            ),
            Agent(
                id='0a481da4-6d89-4d76-b333-0217bc341a50',
                nom='Agent 1',
                email='agent1@example.com',
                actif=False,
            ),
            Agent(
                id='a3c9c21f-23a7-43a0-bbab-65b3c23ae52b',
                nom='Agent 2',
                email='agent2@example.com',
                actif=True,
            ),
            Agent(
                id='4eeeee91-0c11-4175-972e-d158af48cf04',
                nom='Agent 3',
                email='agent3@example.com',
                actif=True,
            ),
            Agent(
                id='3ddf50cc-f826-4cdc-b471-fab321d83aca',
                nom='Agent 4',
                email='agent4@example.com',
                actif=True,
            ),
            Agent(
                id='a33cb3c6-6987-483c-ac12-35cbcbd661c7',
                nom='Agent 5',
                email='agent5@example.com',
                actif=False,
            ),
            Agent(
                id='813277e8-588d-429e-98ce-8d162ed4fe91',
                nom='Agent 6',
                email='agent6@example.com',
                actif=True,
            ),
            Agent(
                id='877948d2-9dce-4d80-b679-53a1fb7fb76c',
                nom='Agent 7',
                email='agent7@example.com',
                actif=True,
            ),
            Agent(
                id='000731c0-9647-4bba-a339-7657de580786',
                nom='Agent 8',
                email='agent8@example.com',
                actif=True,
            ),
            Agent(
                id='b6dafcfc-1462-440a-964c-e78652ef5a61',
                nom='Agent 9',
                email='agent9@example.com',
                actif=True,
            ),
        ]

        # === COMMANDES ===
        commandes = [
            Commande(
                id='8a9e2385-1ce3-4bbf-939c-3b351452244f',
                reference='CMD0000',
                etat='RESERVEE',
            ),
            Commande(
                id='26a81ee6-2f24-422c-90e8-d9754760827b',
                reference='CMD0001',
                etat='EXPEDIEE',
            ),
            Commande(
                id='fa9ee683-77c7-4025-9717-86a56b21d6d8',
                reference='CMD0002',
                etat='ANNULEE',
            ),
            Commande(
                id='d410bda1-81fd-45ab-9c8a-ea43c7342c18',
                reference='CMD0003',
                etat='ANNULEE',
            ),
            Commande(
                id='c5c09e3f-cfa1-4923-aefc-ee8ec82d570a',
                reference='CMD0004',
                etat='RESERVEE',
            ),
            Commande(
                id='d76ccff1-1e21-4e9e-93b3-47862406e692',
                reference='CMD0005',
                etat='ANNULEE',
            ),
            Commande(
                id='c7d43279-5ccf-417b-84f4-c1579c948bbb',
                reference='CMD0006',
                etat='PREPAREE',
            ),
            Commande(
                id='13984242-0939-454b-80ec-73bd7eb9bc58',
                reference='CMD0007',
                etat='EXPEDIEE',
            ),
            Commande(
                id='91ed1c4f-8002-48c7-b101-4cdfe73505d3',
                reference='CMD0008',
                etat='BROUILLON',
            ),
            Commande(
                id='1ea0db4c-0ae4-4bcf-b805-0a6febaec621',
                reference='CMD0009',
                etat='BROUILLON',
            ),
        ]

        lignes_commandes = [
            LigneCommande(
                commande_id='8a9e2385-1ce3-4bbf-939c-3b351452244f',
                article_id='10d55c46-9840-43f0-8dc5-23f8453b16d6',
                quantite=3,
            ),
            LigneCommande(
                commande_id='8a9e2385-1ce3-4bbf-939c-3b351452244f',
                article_id='620d48b8-48ac-4353-9fa6-be268263c56c',
                quantite=1,
            ),
            LigneCommande(
                commande_id='26a81ee6-2f24-422c-90e8-d9754760827b',
                article_id='7a855ef8-ed39-4c8b-9cfa-6696e48a1aa7',
                quantite=2,
            ),
            LigneCommande(
                commande_id='26a81ee6-2f24-422c-90e8-d9754760827b',
                article_id='cef516c1-6599-47c3-a189-7a2fc515037f',
                quantite=6,
            ),
            LigneCommande(
                commande_id='fa9ee683-77c7-4025-9717-86a56b21d6d8',
                article_id='1a4649e4-e6d6-4737-8aa9-c614f558a39f',
                quantite=10,
            ),
        ]

        # === EMPLACEMENTS ===
        emplacements = [
            Emplacement(
                id='f5a27b58-0f0f-4073-87bd-3e2732aa27f0',
                code='E000',
                type='STOCKAGE',
                capacite_poids_kg=181.02,
                capacite_volume_m3=96.19,
            ),
            Emplacement(
                id='285ca606-9542-4c10-8b87-148e0b535c7c',
                code='E001',
                type='EXPEDITION',
                capacite_poids_kg=503.63,
                capacite_volume_m3=16.14,
            ),
            Emplacement(
                id='221665da-d034-483d-a388-d9ef7d4b8b6a',
                code='E002',
                type='STOCKAGE',
                capacite_poids_kg=153.17,
                capacite_volume_m3=99.48,
            ),
            Emplacement(
                id='2b218733-793b-4adb-b512-2ae65704d21f',
                code='E003',
                type='EXPEDITION',
                capacite_poids_kg=676.42,
                capacite_volume_m3=70.04,
            ),
            Emplacement(
                id='a4cd6a47-8400-4023-9f78-5aaab307d5cd',
                code='E004',
                type='VENTE',
                capacite_poids_kg=937.68,
                capacite_volume_m3=26.29,
            ),
            Emplacement(
                id='1bc474c1-da11-4a93-b7e5-71b2dca2bfbf',
                code='E005',
                type='VENTE',
                capacite_poids_kg=555.7,
                capacite_volume_m3=20.19,
            ),
            Emplacement(
                id='4afd9b59-a690-49e3-9eff-be15cd74ff92',
                code='E006',
                type='EXPEDITION',
                capacite_poids_kg=923.41,
                capacite_volume_m3=48.89,
            ),
            Emplacement(
                id='0eaea433-9fc5-4d05-94b1-85a55671a20c',
                code='E007',
                type='EXPEDITION',
                capacite_poids_kg=287.92,
                capacite_volume_m3=41.83,
            ),
            Emplacement(
                id='b36f1ccd-d539-478e-98e2-a2014a848bdb',
                code='E008',
                type='STOCKAGE',
                capacite_poids_kg=650.51,
                capacite_volume_m3=44.63,
            ),
            Emplacement(
                id='d0df5365-381c-4e1c-b43d-2b42fa0b5e46',
                code='E009',
                type='STOCKAGE',
                capacite_poids_kg=187.92,
                capacite_volume_m3=33.72,
            ),
            Emplacement(
                id='5cbce813-0dd6-4cad-8e6a-4753c3bdc7a6',
                code='E010',
                type='RECEPTION',
                capacite_poids_kg=572.2,
                capacite_volume_m3=14.57,
            ),
            Emplacement(
                id='1affe82c-f915-4b89-8b77-15e7f26443b7',
                code='E011',
                type='STOCKAGE',
                capacite_poids_kg=769.66,
                capacite_volume_m3=88.46,
            ),
            Emplacement(
                id='6bd80f8f-cabf-4e7b-8cf6-95a6526482b5',
                code='E012',
                type='RESERVATION',
                capacite_poids_kg=872.93,
                capacite_volume_m3=68.28,
            ),
            Emplacement(
                id='d92cea28-e357-493e-8260-ef6f3223a089',
                code='E013',
                type='RECEPTION',
                capacite_poids_kg=290.35,
                capacite_volume_m3=91.53,
            ),
            Emplacement(
                id='c8a14fc7-93ee-4b5c-a37b-02e665531583',
                code='E014',
                type='RECEPTION',
                capacite_poids_kg=489.59,
                capacite_volume_m3=37.14,
            ),
            Emplacement(
                id='f78aa08c-3c74-436a-a4de-de8998dd4873',
                code='E015',
                type='RECEPTION',
                capacite_poids_kg=434.64,
                capacite_volume_m3=79.93,
            ),
            Emplacement(
                id='cf5ac9f7-6868-418a-b203-0d66b8121b73',
                code='E016',
                type='RESERVATION',
                capacite_poids_kg=443.0,
                capacite_volume_m3=10.58,
            ),
            Emplacement(
                id='39a57bde-1a4a-458b-be4e-838be3b36653',
                code='E017',
                type='VENTE',
                capacite_poids_kg=357.49,
                capacite_volume_m3=14.21,
            ),
            Emplacement(
                id='eaaf8ea9-2c7f-4833-af37-38753d07eb75',
                code='E018',
                type='STOCKAGE',
                capacite_poids_kg=728.53,
                capacite_volume_m3=90.78,
            ),
            Emplacement(
                id='39e20487-6572-40e8-b529-f9609d2db4f5',
                code='E019',
                type='VENTE',
                capacite_poids_kg=669.77,
                capacite_volume_m3=98.26,
            ),
            Emplacement(
                id='6eeaa78b-a036-43a6-9461-e6ba9c0e9414',
                code='E020',
                type='EXPEDITION',
                capacite_poids_kg=866.28,
                capacite_volume_m3=85.03,
            ),
            Emplacement(
                id='444109d0-2356-4309-94d3-277a38bb4f2e',
                code='E021',
                type='EXPEDITION',
                capacite_poids_kg=114.42,
                capacite_volume_m3=39.61,
            ),
            Emplacement(
                id='a26c13a1-701b-4aa5-a880-66023a335be0',
                code='E022',
                type='VENTE',
                capacite_poids_kg=819.88,
                capacite_volume_m3=66.42,
            ),
            Emplacement(
                id='382b9042-3282-48d7-b6b8-0b82fc9cb3bd',
                code='E023',
                type='RESERVATION',
                capacite_poids_kg=735.92,
                capacite_volume_m3=51.57,
            ),
            Emplacement(
                id='d98919b7-0607-4438-b4a4-b234e148c8a2',
                code='E024',
                type='RECEPTION',
                capacite_poids_kg=562.77,
                capacite_volume_m3=22.69,
            ),
            Emplacement(
                id='949b2628-f189-4298-b572-93abcf052978',
                code='E025',
                type='RESERVATION',
                capacite_poids_kg=304.68,
                capacite_volume_m3=63.78,
            ),
            Emplacement(
                id='ac001027-0e9e-4082-90c8-4593224c3fa4',
                code='E026',
                type='EXPEDITION',
                capacite_poids_kg=156.15,
                capacite_volume_m3=92.09,
            ),
            Emplacement(
                id='2decffe1-db24-4fb2-9062-8bf8e7114c36',
                code='E027',
                type='EXPEDITION',
                capacite_poids_kg=204.74,
                capacite_volume_m3=27.05,
            ),
            Emplacement(
                id='75294edd-a03d-4dd0-bca5-c4d354d4bd16',
                code='E028',
                type='EXPEDITION',
                capacite_poids_kg=298.36,
                capacite_volume_m3=81.41,
            ),
            Emplacement(
                id='02da0309-b150-4733-b9c5-0c26ff5cedf2',
                code='E029',
                type='STOCKAGE',
                capacite_poids_kg=472.54,
                capacite_volume_m3=38.49,
            ),
        ]

        # === IMPLANTATIONS ===
        implantations = [
            Implantation(
                id='2205a0b6-ab41-45f0-b98a-e0868231fc7a',
                article_id='620d48b8-48ac-4353-9fa6-be268263c56c',
                emplacement_id='39a57bde-1a4a-458b-be4e-838be3b36653',
                quantite=89,
                seuil_minimum=18,
            ),
            Implantation(
                id='12c95904-dd71-479a-aeb3-64afb96c5dd0',
                article_id='168a6854-579d-4838-a9c4-3c5679bc677a',
                emplacement_id='d0df5365-381c-4e1c-b43d-2b42fa0b5e46',
                quantite=90,
                seuil_minimum=12,
            ),
            Implantation(
                id='669abd4c-fad2-41c2-b48d-9e941dfe21a2',
                article_id='6d5c4080-8b1a-4a37-9c32-7e9d1bfe0d40',
                emplacement_id='ac001027-0e9e-4082-90c8-4593224c3fa4',
                quantite=58,
                seuil_minimum=6,
            ),
            Implantation(
                id='d9178348-80fb-4c97-8cce-dcaf712ed84d',
                article_id='774e9f91-957c-48f1-8e40-810f6b161cf3',
                emplacement_id='2decffe1-db24-4fb2-9062-8bf8e7114c36',
                quantite=96,
                seuil_minimum=9,
            ),
            Implantation(
                id='1818f53e-196b-4d54-be62-33be0f07e3f4',
                article_id='05a602fc-ec0c-43d7-a0fb-f2f1824e9d69',
                emplacement_id='39e20487-6572-40e8-b529-f9609d2db4f5',
                quantite=27,
                seuil_minimum=17,
            ),
            Implantation(
                id='a7d4b832-5852-4e2e-a1ba-a902297f2205',
                article_id='a9a90b6d-b4cc-4e68-b222-6578f3ae3502',
                emplacement_id='444109d0-2356-4309-94d3-277a38bb4f2e',
                quantite=21,
                seuil_minimum=10,
            ),
            Implantation(
                id='49892d9d-ccd3-4860-aaf8-31dd47b1652a',
                article_id='3bc80159-d354-43d9-9085-0bb1a54d6856',
                emplacement_id='2b218733-793b-4adb-b512-2ae65704d21f',
                quantite=49,
                seuil_minimum=6,
            ),
            Implantation(
                id='cf1258de-5e14-49fe-8af9-0c45bf1987c0',
                article_id='7a855ef8-ed39-4c8b-9cfa-6696e48a1aa7',
                emplacement_id='6eeaa78b-a036-43a6-9461-e6ba9c0e9414',
                quantite=96,
                seuil_minimum=17,
            ),
            Implantation(
                id='7b12aea5-1e04-4552-b62a-4a71ffe28ac9',
                article_id='da3d5688-0748-4461-ab27-5932b707d18f',
                emplacement_id='1bc474c1-da11-4a93-b7e5-71b2dca2bfbf',
                quantite=13,
                seuil_minimum=19,
            ),
            Implantation(
                id='add5ba54-8624-4c3c-812e-cd3f3f68502e',
                article_id='da3d5688-0748-4461-ab27-5932b707d18f',
                emplacement_id='39a57bde-1a4a-458b-be4e-838be3b36653',
                quantite=18,
                seuil_minimum=14,
            ),
            Implantation(
                id='7799d8b0-5218-41c2-aa3f-a1a232c4a6a9',
                article_id='395b92df-ca7a-46b4-b3e7-9e3513248c60',
                emplacement_id='949b2628-f189-4298-b572-93abcf052978',
                quantite=10,
                seuil_minimum=14,
            ),
            Implantation(
                id='1f3278b6-7cb4-4580-8f80-b97c2b799ed4',
                article_id='cef516c1-6599-47c3-a189-7a2fc515037f',
                emplacement_id='5cbce813-0dd6-4cad-8e6a-4753c3bdc7a6',
                quantite=9,
                seuil_minimum=16,
            ),
            Implantation(
                id='b4ed8c8b-dca0-4e92-ab88-a26be91b742c',
                article_id='3bc80159-d354-43d9-9085-0bb1a54d6856',
                emplacement_id='eaaf8ea9-2c7f-4833-af37-38753d07eb75',
                quantite=53,
                seuil_minimum=15,
            ),
            Implantation(
                id='05203a45-680c-4695-999e-fe6bfa347772',
                article_id='a9a90b6d-b4cc-4e68-b222-6578f3ae3502',
                emplacement_id='6bd80f8f-cabf-4e7b-8cf6-95a6526482b5',
                quantite=56,
                seuil_minimum=13,
            ),
            Implantation(
                id='1fe4ba1a-b8fe-4bf3-b7bd-c1df9c8be75a',
                article_id='7a855ef8-ed39-4c8b-9cfa-6696e48a1aa7',
                emplacement_id='d98919b7-0607-4438-b4a4-b234e148c8a2',
                quantite=25,
                seuil_minimum=11,
            ),
            Implantation(
                id='0dd1aec5-594f-4304-81d4-517058b3bbdf',
                article_id='10d55c46-9840-43f0-8dc5-23f8453b16d6',
                emplacement_id='6bd80f8f-cabf-4e7b-8cf6-95a6526482b5',
                quantite=7,
                seuil_minimum=20,
            ),
            Implantation(
                id='795fd198-cd0a-4b15-bc69-499d6f35170c',
                article_id='05a602fc-ec0c-43d7-a0fb-f2f1824e9d69',
                emplacement_id='cf5ac9f7-6868-418a-b203-0d66b8121b73',
                quantite=45,
                seuil_minimum=8,
            ),
            Implantation(
                id='b89e10e0-620b-4d8a-969d-0ec86e3f8e5e',
                article_id='1a4649e4-e6d6-4737-8aa9-c614f558a39f',
                emplacement_id='6bd80f8f-cabf-4e7b-8cf6-95a6526482b5',
                quantite=53,
                seuil_minimum=8,
            ),
            Implantation(
                id='b0ee6f90-9bc2-45c9-a7a9-9b92f5f2e63e',
                article_id='6c572a1c-bc0a-4bd5-ae62-460600c6ed23',
                emplacement_id='d98919b7-0607-4438-b4a4-b234e148c8a2',
                quantite=89,
                seuil_minimum=15,
            ),
            Implantation(
                id='28facd27-6fc4-485e-a59f-f492c4e01d02',
                article_id='da3d5688-0748-4461-ab27-5932b707d18f',
                emplacement_id='949b2628-f189-4298-b572-93abcf052978',
                quantite=80,
                seuil_minimum=9,
            ),
        ]

        # === MISSIONS ===
        missions = [
            Mission(
                id='1c51e15a-7e66-493a-a513-522c40811fab',
                type='INVENTAIRE',
                etat='TERMINE',
                article_id='1f5b5fe1-7048-479a-9027-56dfbfd796e2',
                source_id='1bc474c1-da11-4a93-b7e5-71b2dca2bfbf',
                destination_id='1affe82c-f915-4b89-8b77-15e7f26443b7',
                quantite=42,
                agent_id='a3c9c21f-23a7-43a0-bbab-65b3c23ae52b',
                date_creation=datetime(2024, 4, 7, 0, 0),
                date_execution=None,
            ),
            Mission(
                id='0a7d4367-0ad7-469f-97c6-8ce47a13a70f',
                type='DEPLACEMENT',
                etat='TERMINE',
                article_id='10d55c46-9840-43f0-8dc5-23f8453b16d6',
                source_id='02da0309-b150-4733-b9c5-0c26ff5cedf2',
                destination_id='285ca606-9542-4c10-8b87-148e0b535c7c',
                quantite=49,
                agent_id='0a481da4-6d89-4d76-b333-0217bc341a50',
                date_creation=datetime(2024, 11, 30, 0, 0),
                date_execution=None,
            ),
            Mission(
                id='e7f48221-71bb-486e-a253-bb07171ef62d',
                type='RECEPTION',
                etat='TERMINE',
                article_id='1a4649e4-e6d6-4737-8aa9-c614f558a39f',
                source_id='6bd80f8f-cabf-4e7b-8cf6-95a6526482b5',
                destination_id='0eaea433-9fc5-4d05-94b1-85a55671a20c',
                quantite=8,
                agent_id='17ec87fd-6f24-4e2c-a6b6-7928025a94b3',
                date_creation=datetime(2024, 11, 26, 0, 0),
                date_execution=datetime(2024, 3, 29, 0, 0),
            ),
            Mission(
                id='c0156c98-d60d-4b72-9c30-fdaf0b97beeb',
                type='INVENTAIRE',
                etat='ECHOUE',
                article_id='fbdc7d09-7169-42e1-905f-fcfbacb91fc3',
                source_id='b36f1ccd-d539-478e-98e2-a2014a848bdb',
                destination_id='6bd80f8f-cabf-4e7b-8cf6-95a6526482b5',
                quantite=6,
                agent_id='000731c0-9647-4bba-a339-7657de580786',
                date_creation=datetime(2025, 3, 1, 0, 0),
                date_execution=datetime(2024, 9, 17, 0, 0),
            ),
            Mission(
                id='67672152-1b97-48d9-82c1-a9a8fcdd2417',
                type='DEPLACEMENT',
                etat='TERMINE',
                article_id='cef516c1-6599-47c3-a189-7a2fc515037f',
                source_id='1bc474c1-da11-4a93-b7e5-71b2dca2bfbf',
                destination_id='285ca606-9542-4c10-8b87-148e0b535c7c',
                quantite=21,
                agent_id='a33cb3c6-6987-483c-ac12-35cbcbd661c7',
                date_creation=datetime(2024, 4, 16, 0, 0),
                date_execution=None,
            ),
            Mission(
                id='11032bca-3dcb-4fe0-9cdb-598fe97aa326',
                type='PREPARATION',
                etat='TERMINE',
                article_id='4d0b10ae-6a0b-4c96-9f54-6b511952f5d6',
                source_id='f5a27b58-0f0f-4073-87bd-3e2732aa27f0',
                destination_id='f5a27b58-0f0f-4073-87bd-3e2732aa27f0',
                quantite=43,
                agent_id='b6dafcfc-1462-440a-964c-e78652ef5a61',
                date_creation=datetime(2025, 8, 11, 0, 0),
                date_execution=datetime(2025, 7, 5, 0, 0),
            ),
            Mission(
                id='62156b77-c0ca-442a-bbc6-ac6bff421ce2',
                type='PREPARATION',
                etat='TERMINE',
                article_id='05a602fc-ec0c-43d7-a0fb-f2f1824e9d69',
                source_id='f78aa08c-3c74-436a-a4de-de8998dd4873',
                destination_id='2decffe1-db24-4fb2-9062-8bf8e7114c36',
                quantite=45,
                agent_id='0a481da4-6d89-4d76-b333-0217bc341a50',
                date_creation=datetime(2025, 7, 28, 0, 0),
                date_execution=datetime(2025, 5, 23, 0, 0),
            ),
            Mission(
                id='a875b8d6-b90d-4051-a03c-0637a7166e1a',
                type='PREPARATION',
                etat='A_FAIRE',
                article_id='3bc80159-d354-43d9-9085-0bb1a54d6856',
                source_id='382b9042-3282-48d7-b6b8-0b82fc9cb3bd',
                destination_id='b36f1ccd-d539-478e-98e2-a2014a848bdb',
                quantite=6,
                agent_id='a3c9c21f-23a7-43a0-bbab-65b3c23ae52b',
                date_creation=datetime(2024, 3, 30, 0, 0),
                date_execution=None,
            ),
            Mission(
                id='4c91af9d-7a0a-4ae3-8821-dfd7fd33b0ed',
                type='INVENTAIRE',
                etat='ECHOUE',
                article_id='774e9f91-957c-48f1-8e40-810f6b161cf3',
                source_id='0eaea433-9fc5-4d05-94b1-85a55671a20c',
                destination_id='02da0309-b150-4733-b9c5-0c26ff5cedf2',
                quantite=1,
                agent_id='b6dafcfc-1462-440a-964c-e78652ef5a61',
                date_creation=datetime(2024, 9, 15, 0, 0),
                date_execution=datetime(2025, 1, 15, 0, 0),
            ),
            Mission(
                id='fd195061-b9e7-4125-aad1-6260c907c423',
                type='DEPLACEMENT',
                etat='EN_COURS',
                article_id='a9a90b6d-b4cc-4e68-b222-6578f3ae3502',
                source_id='f5a27b58-0f0f-4073-87bd-3e2732aa27f0',
                destination_id='5cbce813-0dd6-4cad-8e6a-4753c3bdc7a6',
                quantite=37,
                agent_id='877948d2-9dce-4d80-b679-53a1fb7fb76c',
                date_creation=datetime(2025, 1, 3, 0, 0),
                date_execution=None,
            ),
        ]

        # === RECEPTIONS ===
        receptions = [
            Reception(
                id='01d2b493-2674-4e3f-9868-0f25b4322de6',
                article_id='620d48b8-48ac-4353-9fa6-be268263c56c',
                quantite=72,
                fournisseur='Fournisseur 0',
                date_reception=datetime(2025, 4, 16, 0, 0),
                emplacement_id='382b9042-3282-48d7-b6b8-0b82fc9cb3bd',
            ),
            Reception(
                id='7477f307-ad47-4da6-a290-fab807305046',
                article_id='10d55c46-9840-43f0-8dc5-23f8453b16d6',
                quantite=41,
                fournisseur='Fournisseur 1',
                date_reception=datetime(2024, 11, 9, 0, 0),
                emplacement_id='39e20487-6572-40e8-b529-f9609d2db4f5',
            ),
            Reception(
                id='bd3ab15c-a8d8-4796-8658-5f8ab76679a8',
                article_id='e0e1ba1c-5e74-4443-896f-d97173e6d75b',
                quantite=71,
                fournisseur='Fournisseur 2',
                date_reception=datetime(2025, 4, 1, 0, 0),
                emplacement_id='02da0309-b150-4733-b9c5-0c26ff5cedf2',
            ),
            Reception(
                id='e2d52599-055d-4b14-a0c0-b65fc3ae13e5',
                article_id='6d5c4080-8b1a-4a37-9c32-7e9d1bfe0d40',
                quantite=62,
                fournisseur='Fournisseur 3',
                date_reception=datetime(2025, 2, 18, 0, 0),
                emplacement_id='4afd9b59-a690-49e3-9eff-be15cd74ff92',
            ),
            Reception(
                id='4d5652e3-6f19-4649-a31d-af53f595180c',
                article_id='774e9f91-957c-48f1-8e40-810f6b161cf3',
                quantite=85,
                fournisseur='Fournisseur 4',
                date_reception=datetime(2024, 5, 17, 0, 0),
                emplacement_id='1bc474c1-da11-4a93-b7e5-71b2dca2bfbf',
            ),
            Reception(
                id='e750013a-68c3-4a5c-91a2-f86648e1aa3b',
                article_id='a9a90b6d-b4cc-4e68-b222-6578f3ae3502',
                quantite=22,
                fournisseur='Fournisseur 5',
                date_reception=datetime(2025, 4, 21, 0, 0),
                emplacement_id='1affe82c-f915-4b89-8b77-15e7f26443b7',
            ),
            Reception(
                id='fe27cad2-1fa7-42b8-a591-d12be4ba1032',
                article_id='a9a90b6d-b4cc-4e68-b222-6578f3ae3502',
                quantite=58,
                fournisseur='Fournisseur 6',
                date_reception=datetime(2024, 12, 10, 0, 0),
                emplacement_id='285ca606-9542-4c10-8b87-148e0b535c7c',
            ),
            Reception(
                id='cbf73abf-ed14-4d38-aebb-b0a8bdd1589a',
                article_id='4d0b10ae-6a0b-4c96-9f54-6b511952f5d6',
                quantite=95,
                fournisseur='Fournisseur 7',
                date_reception=datetime(2025, 4, 17, 0, 0),
                emplacement_id='cf5ac9f7-6868-418a-b203-0d66b8121b73',
            ),
            Reception(
                id='bcf0911b-152b-4bee-8fb7-cb3409c3f7fd',
                article_id='e0e1ba1c-5e74-4443-896f-d97173e6d75b',
                quantite=80,
                fournisseur='Fournisseur 8',
                date_reception=datetime(2025, 9, 18, 0, 0),
                emplacement_id='75294edd-a03d-4dd0-bca5-c4d354d4bd16',
            ),
            Reception(
                id='22293383-e13b-4d27-8068-a04a332f9182',
                article_id='4d0b10ae-6a0b-4c96-9f54-6b511952f5d6',
                quantite=38,
                fournisseur='Fournisseur 9',
                date_reception=datetime(2024, 11, 25, 0, 0),
                emplacement_id='6eeaa78b-a036-43a6-9461-e6ba9c0e9414',
            ),
        ]

        # Ajout global
        db.add_all(articles + agents + commandes + lignes_commandes + emplacements + implantations + missions + receptions)
        db.commit()
        print("Données de test insérées avec succès.")

    except IntegrityError as e:
        db.rollback()
        print("Erreur d'intégrité :", e)
    finally:
        db.close()


def add_new_entries():
    db = SessionLocal()
    try:
        # Create and add a new Article
        new_article = Article(
            id=str(uuid.uuid4()),
            sku='ART1020',
            designation='Nouveau Produit Test',
            categorie='PRODUIT',
            poids_kg=4.75,
            volume_m3=0.325,
            date_peremption=date(2025, 6, 15)
        )

        # Create and add a new Agent
        new_agent = Agent(
            id=str(uuid.uuid4()),
            nom='Agent Test',
            email='agent.test@example.com',
            actif=True
        )

        # Add to database
        db.add(new_article)
        db.add(new_agent)
        db.commit()

        # Print confirmation with IDs
        print(f"Article ajouté avec succès: ID={new_article.id}, SKU={new_article.sku}")
        print(f"Agent ajouté avec succès: ID={new_agent.id}, Nom={new_agent.nom}")

        return new_article.id, new_agent.id

    except Exception as e:
        db.rollback()
        print(f"Erreur lors de l'ajout: {e}")
    finally:
        db.close()


def add_new_reception():
    db = SessionLocal()
    try:
        # Get a random article and emplacement for the reception
        article = db.query(Article).filter(Article.id == '10d55c46-9840-43f0-8dc5-23f8453b16d6').first()
        emplacement = db.query(Emplacement).filter(Emplacement.type == 'RECEPTION').first()

        if not article or not emplacement:
            print("Article or suitable emplacement not found")
            return None

        # Create and add a new Reception
        new_reception = Reception(
            id=str(uuid.uuid4()),
            article_id=article.id,
            quantite=50,
            fournisseur='Fournisseur XYZ',
            date_reception=datetime.now(),
            emplacement_id=emplacement.id
        )

        # Add to database
        db.add(new_reception)
        db.commit()

        # Print confirmation with ID
        print(f"Réception ajoutée avec succès: ID={new_reception.id}")
        print(f"Article: {article.designation} (SKU: {article.sku})")
        print(f"Emplacement: {emplacement.code}")
        print(f"Quantité: {new_reception.quantite}")
        print(f"Date: {new_reception.date_reception}")

        return new_reception.id

    except Exception as e:
        db.rollback()
        print(f"Erreur lors de l'ajout de la réception: {e}")
    finally:
        db.close()


if __name__ == "__main__":
<<<<<<< HEAD
    init_seed_data()
=======
    seed()
    add_new_entries()
<<<<<<< HEAD
>>>>>>> 710f3fd (chore: adding local test data)
=======
    add_new_reception()
>>>>>>> 0b66489 (chore: adding new Reception local test data)
