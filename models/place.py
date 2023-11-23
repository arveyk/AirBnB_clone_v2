#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column(
                          "place_id",
                          String(60),
                          ForeignKey("places.id"),
                          primary_key=True,
                          nullable=False
                          ),
                      Column(
                          "amenity_id", String(60),
                          ForeignKey("amenities.id"),
                          primary_key=True,
                          nullable=False
                          ))


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place',
                           cascade="all, delete, delete-orphan")
    amenity_ids = []

    @property
    def reviews(self):
        """
        Returns the reviews linked to the place.
        """
        from models import storage
        lis = []
        storage.reload()
        for value in storage.all(Review).values():
            if value.__dict__['state_id'] == self.id:
                lis.append(value)
        return lis

    @property
    def amenities(self):
        """
        Returns a list of Amenity instances based on the
        attribute amenity_ids that contains all Amenity.id
        linked to the Place
        """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """
        Appends Amenity objects to the attribute amenity_ids.
        """
        from models.amenity import Amenity
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
