#!/usr/bin/python3
"""
Create State "California" with City "San Francisco"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from model_state import Base  # Base object

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db_name),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and linked City using the relationship
    california = State(name="California")
    california.cities = [City(name="San Francisco")]

    session.add(california)
    session.commit()
    session.close()
