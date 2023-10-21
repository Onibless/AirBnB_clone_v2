#!/usr/bin/python3
"""creating the state table"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """state class

    Args:
        BaseModel (class): parent class
        Base (class): from sqlalchemy

    Returns:
        list: city instances
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """defining cities property

            Returns:
                list: city instances
            """
            values_city = models.storage.all("City").values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
