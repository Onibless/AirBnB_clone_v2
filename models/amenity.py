#!/usr/bin/python3
""" holds class Amenity"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity database """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128),
                      nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity insances"""
        super().__init__(*args, **kwargs)
