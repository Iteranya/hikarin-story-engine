from typing import List, Optional, Dict, Any
from sqlalchemy import String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy
from app.models.asset import Asset
from app.models.base import Base

class CharacterSprite(Base):
    __tablename__ = "character_sprite"
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), primary_key=True, init=False)
    asset_id: Mapped[int] = mapped_column(ForeignKey("asset.id"), primary_key=True, init=False)
    sprite_name: Mapped[str] = mapped_column(String(50))
    emotion: Mapped[Optional[str]] = mapped_column(String(50), default="neutral")
    clothes: Mapped[Optional[str]] = mapped_column(String(50), default="default")
    asset: Mapped["Asset"] = relationship(lazy="joined")

class Character(Base):
    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    slug: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    desc: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    custom: Mapped[Dict[str, Any]] = mapped_column(JSON, default_factory=dict)

    pfp_id: Mapped[Optional[int]] = mapped_column(ForeignKey("asset.id"), default=None, init=False)
    pfp: Mapped[Optional["Asset"]] = relationship(default=None)

    sprites: Mapped[List["CharacterSprite"]] = relationship(default_factory=list, cascade="all, delete-orphan")
    sprite_assets: AssociationProxy[List["Asset"]] = association_proxy("sprites", "asset", init=False)
