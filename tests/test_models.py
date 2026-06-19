import app.models
from app.db.base import Base
from sqlalchemy.orm import configure_mappers


def test_models_are_registered() -> None:
    expected_tables = {
        "financial_categories",
        "financial_transactions",
        "roles",
        "ticket_comments",
        "ticket_status_history",
        "tickets",
        "users",
    }

    assert expected_tables.issubset(Base.metadata.tables.keys())


def test_model_relationships_are_configured() -> None:
    configure_mappers()
