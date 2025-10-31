from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


engine = create_engine(
    "postgresql://postgres:Kolosokelena1%29@localhost:5432/postgres"
)
Session = sessionmaker(bind=engine)
