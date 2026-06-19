from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.ticket_comment import TicketComment
    from app.models.ticket_status_history import TicketStatusHistory
    from app.models.user import User


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    priority: Mapped[str] = mapped_column(
        Enum("low", "medium", "high", "critical", name="ticket_priority"),
        nullable=False,
        server_default=text("'medium'"),
    )
    status: Mapped[str] = mapped_column(
        Enum("open", "in_progress", "resolved", "closed", name="ticket_status"),
        nullable=False,
        server_default=text("'open'"),
    )
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", name="fk_tickets_created_by"),
        nullable=False,
    )
    assigned_to: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", name="fk_tickets_assigned_to"),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    creator: Mapped["User"] = relationship(
        back_populates="created_tickets",
        foreign_keys=[created_by],
    )
    assignee: Mapped["User | None"] = relationship(
        back_populates="assigned_tickets",
        foreign_keys=[assigned_to],
    )
    comments: Mapped[list["TicketComment"]] = relationship(back_populates="ticket")
    status_history: Mapped[list["TicketStatusHistory"]] = relationship(
        back_populates="ticket",
    )
