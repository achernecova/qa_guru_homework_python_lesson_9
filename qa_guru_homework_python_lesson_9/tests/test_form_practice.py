from selene import browser, have

from qa_guru_homework_python_lesson_9.pages.registration_page import RegistrationPage
from qa_guru_homework_python_lesson_9.pages.registration_page_fluent_page_object import (
    RegistrationPageFluentPageObject,
)


def test_filling_out_form_selene():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.type_first_name("Alexandra")
    registration_page.fill_last_name("Chernetsova")
    registration_page.fill_email("achernecova@inbox.ru")
    registration_page.click_gender()
    registration_page.fill_number("8123456789")
    registration_page.fill_birthday("1991", "April", "19")
    registration_page.fill_subject("Biology")
    registration_page.choice_hobby()
    registration_page.upload_image("les.jpg")
    registration_page.fill_address("Москва")
    registration_page.fill_state("Haryana")
    registration_page.fill_city("Karnal")
    registration_page.click_submit()
    browser.element(".modal-title.h4").should(have.text("Thanks for submitting the form"))

    registration_page.registered_user_data.should(
        have.exact_texts(
            "Alexandra Chernetsova",
            "achernecova@inbox.ru",
            "Female",
            "8123456789",
            "19 April,1991",
            "Biology",
            "Reading",
            "les.jpg",
            "Москва",
            "Haryana Karnal",
        )
    )


def test_filling_out_form_selene_with_fluent_page_object():
    registration_page = RegistrationPageFluentPageObject()
    registration_page.open()
    (
        registration_page.type_first_name("Alexandra")
        .fill_last_name("Chernetsova")
        .fill_email("achernecova@inbox.ru")
        .click_gender()
        .fill_number("8123456789")
        .fill_birthday("1991", "April", "19")
        .fill_subject("Biology")
        .choice_hobby()
        .upload_image("les.jpg")
        .fill_address("Москва")
        .fill_state("Haryana")
        .fill_city("Karnal")
        .click_submit()
    )

    registration_page.should_registered_user_info(
        "Alexandra Chernetsova",
        "achernecova@inbox.ru",
        "Female",
        "8123456789",
        "19 April,1991",
        "Biology",
        "Reading",
        "les.jpg",
        "Москва",
        "Haryana Karnal",
    )
