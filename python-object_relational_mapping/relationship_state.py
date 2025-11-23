#!/usr/bin/python3
"""
State class with relationship to City.
Cədvəl artıq mövcud olsa da yenidən istifadə edilə bilər.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base  # Base imported from model_state.py

class State(Base):
    """State class linked to 'states' table with cities relationship"""
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}  # Mövcud cədvələ əlavə etməyə icazə verir

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Relationship to City, cascade delete all linked cities if State deleted
    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")
