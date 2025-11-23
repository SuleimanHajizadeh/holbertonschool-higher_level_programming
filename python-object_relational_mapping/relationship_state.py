#!/usr/bin/python3
"""
State class with relationship to City
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base  # Base imported from model_state.py

class State(Base):
    """State class linked to 'states' table with cities relationship"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Relationship to City, cascade delete all linked cities if State deleted
    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")
