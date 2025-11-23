#!/usr/bin/python3
"""List all State objects and their corresponding City objects"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <user> <password> <db>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Tək sorğu: states və əlaqəli cities
    states = session.query(State).options(joinedload(State.cities)).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"\t{city.id}: {city.name}")

    session.close()
