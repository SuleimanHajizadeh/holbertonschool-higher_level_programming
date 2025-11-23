#!/usr/bin/python3
"""
City class linked to 'cities' table
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base  # Base imported from model_state.py

class City(Base):
    """City class with foreign key to State"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Reference from City to State
    state = relationship("State", back_populates="cities")
