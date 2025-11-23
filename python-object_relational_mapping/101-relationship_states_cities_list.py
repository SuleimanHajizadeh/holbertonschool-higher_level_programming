#!/usr/bin/python3
"""Lists all State objects with their City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <user> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine_url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}"
    engine = create_engine(engine_url)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and their cities in one go, sorted by id
    states = session.query(State).options(joinedload(State.cities))\
        .order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"\t{city.id}: {city.name}")

    session.close()
