#!/usr/bin/python3
""" holds class City"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """Representation of city database"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes city instance"""
        super().__init__(*args, **kwargs)
