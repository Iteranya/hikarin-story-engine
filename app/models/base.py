from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

class Base(DeclarativeBase, MappedAsDataclass):
    """Base class integrating Dataclasses with SQLAlchemy 2.0."""
    pass

# Many-to-Many Association Tables
script_characters = Table(
    "script_characters",
    Base.metadata,
    Column("script_id", ForeignKey("script.id", ondelete="CASCADE"), primary_key=True),
    Column("character_id", ForeignKey("character.id", ondelete="CASCADE"), primary_key=True),
)

script_assets = Table(
    "script_assets",
    Base.metadata,
    Column("script_id", ForeignKey("script.id", ondelete="CASCADE"), primary_key=True),
    Column("asset_id", ForeignKey("asset.id", ondelete="CASCADE"), primary_key=True),
)

script_variables = Table(
    "script_variables",
    Base.metadata,
    Column("script_id", ForeignKey("script.id", ondelete="CASCADE"), primary_key=True),
    Column("variable_id", ForeignKey("variable.id", ondelete="CASCADE"), primary_key=True),
)
