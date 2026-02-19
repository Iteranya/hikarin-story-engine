from typing import List, Optional, Dict, Any
from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.asset import Asset
from app.models.base import Base, script_characters, script_assets, script_variables
from app.models.character import Character
from app.models.variable import Variable

class Script(Base):
    __tablename__ = "script"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    slug: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    desc: Mapped[Optional[str]] = mapped_column(String(255), default=None)

    # Stores the raw DSL text from the writer
    content: Mapped[str] = mapped_column(String, default="")
    custom: Mapped[Dict[str, Any]] = mapped_column(JSON, default_factory=dict)

    characters: Mapped[List["Character"]] = relationship(secondary=script_characters, default_factory=list)
    assets: Mapped[List["Asset"]] = relationship(secondary=script_assets, default_factory=list)
    variables: Mapped[List["Variable"]] = relationship(secondary=script_variables, default_factory=list)
