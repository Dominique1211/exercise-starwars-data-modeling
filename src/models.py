import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    #primary key is so the data base can find it quickly or the index in array 
    id = Column(Integer, primary_key=True)
    #unique means only one person can have this emil 
    #nullable means this cannot be blank
    email = Column(String(128), unique=True, nullable=False)
    name = Column(String(128))
    password = Column(String(128), nullable=False)

# def serialize(self):
#     return {
#         "email": self.email,
#         "name": self.name
#     }

#     @staticmethod
#     def deserialize(data={}):
#         return User(**data)


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=False)  
    skin_color = Column(String(250), nullable=True)
    home_world_id = Column(Integer, ForeignKey('planets.id'))
    home_world = relationship("Planet")



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorite = Column(String(250))

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorite_characters = Column(String(250))

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorite_planets = Column(String(250))
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False) 
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False) 
    surface_water = Column(String(250), nullable=False)
    residents = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)


class favorite_Vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorite_vehicles = Column(String(250))


class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')