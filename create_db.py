import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
from Token import DNS

Base = declarative_base()
engine = sq.create_engine(DNS)

class Publisher(Base):
    __tablename__ = "Suitable_contacts"
    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, nullable=False, unique=True)

    def __str__(self):
        return f"Suitable_contacts {self.user_id} "

def create_tables(engine):
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
create_tables(engine)