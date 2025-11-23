#!/usr/bin/python3
"""
relationship_city module
Defines the City class for SQLAlchemy ORM
linked to State class via foreign key.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base  # Base importu saxlanılır, model_state.py-dan

class City(Base):
    """City class linking to cities table with a foreign key to State"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
