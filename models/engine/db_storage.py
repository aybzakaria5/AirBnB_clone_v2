#!/usr/bin/python3
""" New class for sqlAlchemy DBStorage """
from models.base_model import Base
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import query
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ Create tables in environmental """
    __engine = None
    __session = None

    def __init__(self):
        """ Create new instance of DBStorage """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """ Query all instances of specified class """
        objects = {}
        if cls:
            instances = self.__session.query(cls).all()
        else:
            instances = []
            for model_class in [User, State, City, Amenity, Place, Review]:
                instances.extend(self.__session.query(model_class).all())

        for instance in instances:
            key = "{}.{}".format(instance.__class__.__name__, instance.id)
            objects[key] = instance

        return objects

    def new(self, obj):
        """Add object to current database session."""
        self.__session.add(obj)
        self.save()

    def save(self):
        """Commit all changes of current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session obj if not None."""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Reload all tables and create new session from engine."""
        Base.metadata.create_all(self.__engine)
        sm = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sm)
        self.__session = Session()
