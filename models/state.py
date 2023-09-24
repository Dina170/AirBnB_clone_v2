#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class

    Attributes:
        name (str): state name.

    """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship('City', backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get the list of cities

            Return:
                list.

             """
            cities_objs = list(models.storage.all(City).values())
            return list(filter(lambda obj: obj.state_id == self.id,
                               cities_objs))
