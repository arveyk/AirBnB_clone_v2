#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel(Base):
    """A base class for all hbnb models"""
    __abstract__ = True
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ('created_at', 'updated_at'):
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[k] = v

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        new_dict = self.__dict__.copy()
        del new_dict['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, new_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage."""
        from models import storage
        storage.delete(self)
