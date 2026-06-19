from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.ticket import Ticket
    from app.models.user import User


class TicketStatusHistory(Base):
    __tablename__ = "ticket_status_history"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ticket_id: Mapped[int] = mapped_column(
        ForeignKey("tickets.id", name="fk_ticket_status_history_ticket"),
        nullable=False,
    )
    old_status: Mapped[str | None] = mapped_column(
        Enum("open", "in_progress", "resolved", "closed", name="ticket_old_status"),
        nullable=True,
    )
    new_status: Mapped[str] = mapped_column(
        Enum("open", "in_progress", "resolved", "closed", name="ticket_new_status"),
        nullable=False,
    )
    changed_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", name="fk_ticket_status_history_user"),
        nullable=False,
    )
    changed_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    ticket: Mapped["Ticket"] = relationship(back_populates="status_history")
    changed_by_user: Mapped["User"] = relationship(
        back_populates="ticket_status_changes",
    )
