from models import Base, Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dogs.db')
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()

def create_table(Base, engine):
    if __name__ == '__main__':
        Base.metadata.create.all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()
    return session.query(Dog).first().name


def get_all(session):
    all_dogs = []
    all_dogs = session.query(Dog).all()
    return all_dogs


def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()


def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()


def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()


def update_breed(session, id, breed):
    session.query(Dog).update({Dog.breed: breed})
    session.commit()
