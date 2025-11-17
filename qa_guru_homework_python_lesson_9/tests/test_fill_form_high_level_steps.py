import datetime

from qa_guru_homework_python_lesson_9.pages import users
from qa_guru_homework_python_lesson_9.pages.registration_page import RegistrationPage
from qa_guru_homework_python_lesson_9.pages.users import User
from qa_guru_homework_python_lesson_9.resourses import Gender, Hobbies


def test_fill_form_registration_high_level_steps():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(users.first_user)

    registration_page.should_have_registered(users.first_user)


def test_fill_form_registration_high_level_with_user_in_test():
    first_users = User(
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
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(first_users)
    registration_page.should_have_registered(first_users)
