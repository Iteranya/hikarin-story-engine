from typing import Optional, Dict, Any
from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Asset(Base):
    __tablename__ = "asset"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    slug: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    desc: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    type: Mapped[str] = mapped_column(String(30))  # 'image', 'audio', etc.
    path: Mapped[str] = mapped_column(String(500))
    custom: Mapped[Dict[str, Any]] = mapped_column(JSON, default_factory=dict)
