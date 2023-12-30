#!/usr/bin/python3
"""Write a python file that contains the class definition of a
State and an instance Base
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Args:
        id: row identifier
        name: self explanatory field
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
