import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
from Token import DNS

Base = declarative_base()
engine = sq.create_engine(DNS)

class Publisher(Base):
    __tablename__ = "Contacts_vk"
    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, nullable=False, unique=False)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!primary_key
    first_name = sq.Column(sq.VARCHAR(length=40), nullable=False)
    last_name = sq.Column (sq.VARCHAR(length=40), nullable=False)
    photo_1 = sq.Column(sq.Integer, nullable=False)
    photo_2 = sq.Column (sq.Integer, nullable=False)
    photo_3 = sq.Column (sq.Integer, nullable=False)



    def __str__(self):
        return f"Contact {self.user_id}, Имя: {self.first_name}, Фамилия: {self.last_name},  \
                        фото№1: {self.photo_1},  фото№2: {self.photo_2},  фото№3: {self.photo_3}"

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
create_tables(engine)