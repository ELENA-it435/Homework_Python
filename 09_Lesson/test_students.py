import pytest
from models import Student, Base, engine, Session


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


def test_add_student():
    session = Session()
    student = Student(name="Test Student")
    session.add(student)
    session.commit()

    assert (
        session.query(Student)
        .filter_by(name="Test Student")
        .first() is not None
    )

    session.delete(student)
    session.commit()
    session.close()


def test_update_student():
    session = Session()
    student = Student(name="Old Name")
    session.add(student)
    session.commit()

    student.name = "New Name"
    session.commit()

    updated = session.query(Student).filter_by(id=student.id).first()
    assert updated.name == "New Name"

    session.delete(student)
    session.commit()
    session.close()


def test_delete_student():
    session = Session()
    student = Student(name="Delete Me")
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    assert session.query(Student).filter_by(name="Delete Me").first() is None
    session.close()
