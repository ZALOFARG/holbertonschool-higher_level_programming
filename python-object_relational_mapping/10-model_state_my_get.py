#!/usr/bin/python3
"""Write a script that prints the State object
with the name passed as argument from the database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")
