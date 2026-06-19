from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.financial_transaction import FinancialTransaction
    from app.models.role import Role
    from app.models.ticket import Ticket
    from app.models.ticket_comment import TicketComment
    from app.models.ticket_status_history import TicketStatusHistory


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=text("1"),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id", name="fk_users_roles"),
        nullable=False,
    )

    role: Mapped["Role"] = relationship(back_populates="users")
    financial_transactions: Mapped[list["FinancialTransaction"]] = relationship(
        back_populates="user",
    )
    created_tickets: Mapped[list["Ticket"]] = relationship(
        back_populates="creator",
        foreign_keys="Ticket.created_by",
    )
    assigned_tickets: Mapped[list["Ticket"]] = relationship(
        back_populates="assignee",
        foreign_keys="Ticket.assigned_to",
    )
    ticket_comments: Mapped[list["TicketComment"]] = relationship(
        back_populates="user",
    )
    ticket_status_changes: Mapped[list["TicketStatusHistory"]] = relationship(
        back_populates="changed_by_user",
    )
