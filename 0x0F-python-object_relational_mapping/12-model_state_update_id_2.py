#!/usr/bin/python3

"""
script that changes the name of a State object
from the database hbtn_0e_6_usa via SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to the MySQL server
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database}')

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the state
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
