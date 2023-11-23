#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Amenity(BaseModel, Base):
    from models.place import place_amenity
    __tablename__ = "amenities"
    
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
            secondary=place_amenity, back_populates='amenities')
