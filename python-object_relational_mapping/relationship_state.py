#!/usr/bin/python3
"""
relationship_state module
Defines the State class for SQLAlchemy ORM
with a relationship to the City class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base  # Base importu saxlanılır, model_state.py-dan

class State(Base):
    """State class linking to states table with a relationship to City"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete, delete-orphan"
    )
