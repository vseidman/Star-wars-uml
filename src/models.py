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
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

    
   
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    eye_color = Column(String(200), nullable=False)
    skin_color = Column(String(200), nullable=False)
    location = Column(String(200), nullable=False)
    more_info_button = Column(Integer)
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    population = Column(String(200), nullable=False)
    terrain = Column(String(200), nullable=False)
    climate = Column(String(200), nullable=False)
    more_info_button = Column(Integer)
    

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    like_id = Column(Integer, nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    characters = relationship(Characters)
    planets = relationship(Planets)
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')