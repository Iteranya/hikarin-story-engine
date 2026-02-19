from typing import List, Optional, Dict, Any
from sqlalchemy import String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy
from app.models.base import Base

class VariableLabel(Base):
    __tablename__ = "variable_label"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    variable_id: Mapped[int] = mapped_column(ForeignKey("variable.id"), init=False)
    text: Mapped[str] = mapped_column(String(50))

class Variable(Base):
    __tablename__ = "variable"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    slug: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    desc: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    type: Mapped[str] = mapped_column(String(20))
    default_val: Mapped[str] = mapped_column(String, default="")
    custom: Mapped[Dict[str, Any]] = mapped_column(JSON, default_factory=dict)

    _label_objs: Mapped[List["VariableLabel"]] = relationship(default_factory=list, cascade="all, delete-orphan", init=False)
    labels: AssociationProxy[List[str]] = association_proxy("_label_objs", "text", creator=lambda val: VariableLabel(text=val), default_factory=list)
