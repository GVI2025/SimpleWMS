from fastapi.testclient import TestClient
from unittest.mock import patch, ANY
from datetime import date

from app.main import app
from app.schemas.article import ArticleCreate, ArticleUpdate, CategorieArticle
from app.models import Article as ArticleModel

client = TestClient(app)

# Mock article data
mock_article_data = {
    "id": "12345",
    "sku": "ART001",
    "designation": "Article Test",
    "categorie": CategorieArticle.PRODUIT,
    "poids_kg": 1.5,
    "volume_m3": 0.5,
    "date_peremption": date(2025, 12, 31)
}

mock_article_create = ArticleCreate(
    sku="ART001",
    designation="Article Test",
    categorie=CategorieArticle.PRODUIT,
    poids_kg=1.5,
    volume_m3=0.5,
    date_peremption=date(2025, 12, 31)
)

mock_article_update = ArticleUpdate(
    sku="ART001",
    designation="Article Test Updated",
    categorie=CategorieArticle.PRODUIT,
    poids_kg=2.0,
    volume_m3=0.6,
    date_peremption=date(2026, 1, 15)
)

mock_article_model = ArticleModel(
    id="12345",
    sku="ART001",
    designation="Article Test",
    categorie=CategorieArticle.PRODUIT,
    poids_kg=1.5,
    volume_m3=0.5,
    date_peremption=date(2025, 12, 31)
)

mock_article_list = [
    ArticleModel(
        id="12345",
        sku="ART001",
        designation="Article Test",
        categorie=CategorieArticle.PRODUIT,
        poids_kg=1.5,
        volume_m3=0.5,
        date_peremption=date(2025, 12, 31)
    ),
    ArticleModel(
        id="67890",
        sku="ART002",
        designation="Article Test 2",
        categorie=CategorieArticle.CONSOMMABLE,
        poids_kg=0.5,
        volume_m3=0.2,
        date_peremption=None
    )
]


class TestArticleRouter:
    @patch('app.routers.article.article_service.list_articles')
    def test_list_articles(self, mock_list_articles):
        # Configure mock
        mock_list_articles.return_value = mock_article_list

        # Test the endpoint
        response = client.get("/articles/")

        # Verify response
        assert response.status_code == 200
        assert len(response.json()) == 2

        # Verify service function was called
        mock_list_articles.assert_called_once()

    @patch('app.routers.article.article_service.get_article_by_sku')
    @patch('app.routers.article.article_service.create_article')
    def test_create_article_success(self, mock_create_article, mock_get_by_sku):
        # Configure mocks
        mock_get_by_sku.return_value = None
        mock_create_article.return_value = mock_article_model

        # Test the endpoint
        response = client.post("/articles/", json={
            "sku": "ART001",
            "designation": "Article Test",
            "categorie": "Produit fini",
            "poids_kg": 1.5,
            "volume_m3": 0.5,
            "date_peremption": "2025-12-31"
        })

        # Verify response
        assert response.status_code == 200
        assert response.json()["sku"] == "ART001"

        # Verify service functions were called correctly
        mock_get_by_sku.assert_called_once_with(ANY, "ART001")
        mock_create_article.assert_called_once()

    @patch('app.routers.article.article_service.get_article_by_sku')
    def test_create_article_duplicate_sku(self, mock_get_by_sku):
        # Configure mock to simulate duplicate SKU
        mock_get_by_sku.return_value = mock_article_model

        # Test the endpoint
        response = client.post("/articles/", json={
            "sku": "ART001",
            "designation": "Article Test",
            "categorie": "Produit fini",
            "poids_kg": 1.5,
            "volume_m3": 0.5,
            "date_peremption": "2025-12-31"
        })

        # Verify response
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    @patch('app.routers.article.article_service.get_article')
    def test_get_article_success(self, mock_get_article):
        # Configure mock
        mock_get_article.return_value = mock_article_model

        # Test the endpoint
        response = client.get(f"/articles/{mock_article_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_article_data["id"]

        # Verify service function was called correctly
        mock_get_article.assert_called_once_with(ANY, mock_article_data["id"])

    @patch('app.routers.article.article_service.get_article')
    def test_get_article_not_found(self, mock_get_article):
        # Configure mock
        mock_get_article.return_value = None

        # Test the endpoint
        response = client.get("/articles/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.article.article_service.update_article')
    def test_update_article_success(self, mock_update_article):
        # Configure mock
        updated_article = mock_article_model
        updated_article.designation = "Article Test Updated"
        updated_article.poids_kg = 2.0
        mock_update_article.return_value = updated_article

        # Test the endpoint
        response = client.put(
            f"/articles/{mock_article_data['id']}",
            json={
                "sku": "ART001",
                "designation": "Article Test Updated",
                "categorie": "Produit fini",
                "poids_kg": 2.0,
                "volume_m3": 0.5,
                "date_peremption": "2025-12-31"
            }
        )

        # Verify response
        assert response.status_code == 200
        assert response.json()["designation"] == "Article Test Updated"
        assert response.json()["poids_kg"] == 2.0

        # Verify service function was called correctly
        mock_update_article.assert_called_once()

    @patch('app.routers.article.article_service.update_article')
    def test_update_article_not_found(self, mock_update_article):
        # Configure mock
        mock_update_article.return_value = None

        # Test the endpoint
        response = client.put(
            "/articles/nonexistent",
            json={
                "sku": "ART001",
                "designation": "Article Test Updated",
                "categorie": "Produit fini",
                "poids_kg": 2.0,
                "volume_m3": 0.5,
                "date_peremption": "2025-12-31"
            }
        )

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

    @patch('app.routers.article.article_service.delete_article')
    def test_delete_article_success(self, mock_delete_article):
        # Configure mock
        mock_delete_article.return_value = mock_article_model

        # Test the endpoint
        response = client.delete(f"/articles/{mock_article_data['id']}")

        # Verify response
        assert response.status_code == 200
        assert response.json()["id"] == mock_article_data["id"]

        # Verify service function was called correctly
        mock_delete_article.assert_called_once_with(ANY, mock_article_data["id"])

    @patch('app.routers.article.article_service.delete_article')
    def test_delete_article_not_found(self, mock_delete_article):
        # Configure mock
        mock_delete_article.return_value = None

        # Test the endpoint
        response = client.delete("/articles/nonexistent")

        # Verify response
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]