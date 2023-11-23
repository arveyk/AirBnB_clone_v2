#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
#from models import storage


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Returns the list of City instances with state_id \
            equals to the current State.id"""
        from models import storage
        lis = []
        storage.reload()
        for value in storage.all(City).values():
            if value.__dict__['state_id'] == self.id:
                lis.append(value)
        return lis
