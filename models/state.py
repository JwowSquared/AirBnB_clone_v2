#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
engine = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if engine == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states", cascade="all, delete")

    if engine == "fs":
        @property
        def cities(self):
            """getter for FileStorage use"""
            # potentially need to encase this in an if statement to protect
            from models import storage
            from models.city import City
            out = []
            for obj in storage.all(City).values():
                if obj.state_id == self.id:
                    out.append(obj)
            return out
