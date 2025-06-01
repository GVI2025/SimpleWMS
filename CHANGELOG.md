# [1.0.0] (2025-01-01)

### Added

- **Article Management**: Add, edit, delete, and list/search articles.
- **Emplacement Management**: Create and manage emplacement zones with capacity definitions.
- **Reception Workflow**: Register receptions of articles from suppliers and link them to emplacements.
- **Stock Implantation**: Define implantation of articles in emplacements with minimum thresholds and display implantation details.
- **Order Management**: Create orders with multiple articles and quantities, and track order statuses.
- **Mission Handling**: Create missions for operations (move, restock, inventory, reception, order preparation), assign missions to agents, and track mission statuses.
- **Agent Management**: Add, edit, remove agents, and activate/deactivate agent accounts.
- REST API endpoints for all core entities and workflows.
- Database schema and migrations using Alembic.
- Initial data seeding script for testing purposes.
- FastAPI-based application with Swagger UI for API documentation.