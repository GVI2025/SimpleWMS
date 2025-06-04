import pytest
from unittest.mock import MagicMock, call
from app.services.mission import list_missions
from app.models import Mission as MissionModel
from sqlalchemy.sql.elements import BinaryExpression

@pytest.fixture
def mock_db():
    return MagicMock()

def test_list_missions_filters_out_failed_and_finished(mock_db):
    # Arrange
    mock_query = mock_db.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_offset = mock_filter.offset.return_value
    mock_limit = mock_offset.limit.return_value
    mock_limit.all.return_value = ['mission1', 'mission2']

    # Act
    result = list_missions(mock_db, skip=5, limit=10)

    # Assert
    mock_db.query.assert_called_once_with(MissionModel)
    # Check that filter was called once with two BinaryExpression objects
    assert mock_query.filter.call_count == 1
    args, kwargs = mock_query.filter.call_args
    assert len(args) == 2
    for expr, value in zip(args, ["Échoué", "Terminé"]):
        assert isinstance(expr, BinaryExpression)
        assert expr.left.name == "etat"
        assert expr.right.value == value
        assert expr.operator.__name__ == "ne"  # 'ne' means 'not equal'
    mock_filter.offset.assert_called_once_with(5)
    mock_offset.limit.assert_called_once_with(10)
    mock_limit.all.assert_called_once()
    assert result == ['mission1', 'mission2']

def test_list_missions_default_skip_and_limit(mock_db):
    mock_query = mock_db.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_offset = mock_filter.offset.return_value
    mock_limit = mock_offset.limit.return_value
    mock_limit.all.return_value = []

    result = list_missions(mock_db)

    mock_filter.offset.assert_called_once_with(0)
    mock_offset.limit.assert_called_once_with(100)
    assert result == []