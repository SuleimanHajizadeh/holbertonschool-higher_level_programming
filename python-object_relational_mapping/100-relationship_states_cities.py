#!/usr/bin/python3
"""
100-relationship_states_cities module
Creates a State 'California' with a City 'San Francisco'
and links them using SQLAlchemy relationships.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> <password> <database>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # State və City yaratmaq
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    session.add(california)
    session.commit()
    session.close()
