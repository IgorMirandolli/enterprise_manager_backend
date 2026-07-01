"""baseline existing schema

Revision ID: a44392746a14
Revises: 
Create Date: 2026-07-01 10:26:17.794119
"""

from collections.abc import Sequence

revision: str = 'a44392746a14'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Baseline for tables created manually before Alembic was configured.
    pass


def downgrade() -> None:
    # This baseline does not create or drop existing tables.
    pass
