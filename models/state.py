#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import models
from models.city import City
from sqlalchemy.orm import relationship
import shlex

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        ins = models.storage.all()
        listc = []
        res = []
        for key in ins:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                listc.append(ins[key])
        for elm in listc:
            res.append(elm)
        return (res)
