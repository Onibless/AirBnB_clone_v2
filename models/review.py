#!/usr/bin/python3
"""setting up eviews table
"""
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """Representation of Review table"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024),
                      nullable=False)
        place_id = Column(String(60),
                          ForeignKey('places.id'),
                          nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id'),
                         nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Review instances"""
        super().__init__(*args, **kwargs)
