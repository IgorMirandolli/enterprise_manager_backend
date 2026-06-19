from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, Enum, ForeignKey, Numeric, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.financial_category import FinancialCategory
    from app.models.user import User


class FinancialTransaction(Base):
    __tablename__ = "financial_transactions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(String(150), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    type: Mapped[str] = mapped_column(
        Enum("income", "expense", name="financial_transaction_type"),
        nullable=False,
    )
    transaction_date: Mapped[date] = mapped_column(Date, nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("financial_categories.id", name="fk_transactions_categories"),
        nullable=False,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", name="fk_transactions_users"),
        nullable=False,
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    category: Mapped["FinancialCategory"] = relationship(
        back_populates="transactions",
    )
    user: Mapped["User"] = relationship(back_populates="financial_transactions")
