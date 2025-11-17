import datetime
from dataclasses import dataclass

from qa_guru_homework_python_lesson_9.resourses import Gender, Hobbies


@dataclass
class User:
    firstname: str
    lastname: str
    email: str
    gender: Gender
    phone: str
    birthday: datetime.date
    subject: str
    hobbies: Hobbies
    picture: str
    address: str
    state: str
    city: str


first_user = User(
    firstname="Alexandra",
    lastname="Chernetsova",
    email="achernecova@inbox.ru",
    gender=Gender.FEMALE,
    phone="8123456789",
    birthday=datetime.date(1991, 4, 19),
    subject="Biology",
    hobbies=Hobbies.READING,
    picture="les.jpg",
    address="Москва",
    state="Haryana",
    city="Karnal",
)
