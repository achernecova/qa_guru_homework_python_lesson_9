from selene import be, browser, command, have
from selenium.webdriver.common.by import By

from qa_guru_homework_python_lesson_9.resourses import resource_path


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.all(
            ".modal-content table tbody tr td:nth-child(2)"
        )

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    @staticmethod
    def type_first_name(name):
        browser.element("#firstName").type(name)

    @staticmethod
    def fill_birthday(year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(
            f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month"
        ).click()

    # @property
    # def registered_user_data(self):
    #     return browser.all('.modal-content table tbody tr td:nth-child(2)')

    @staticmethod
    def fill_state(state):
        browser.element("#state").perform(command.js.scroll_into_view).click()
        browser.element("#react-select-3-input").type(state).press_enter()

    @staticmethod
    def fill_city(city):
        browser.element("#city").click()
        browser.element("#react-select-4-input").send_keys(city).press_enter()

    @staticmethod
    def fill_last_name(last_name):
        browser.element("#lastName").type(last_name)

    @staticmethod
    def fill_email(email):
        browser.element("#userEmail").type(email)

    @staticmethod
    def click_gender():
        browser.element('[for="gender-radio-2"]').should(be.clickable).click()

    @staticmethod
    def fill_number(number):
        browser.element("#userNumber").type(number)

    @staticmethod
    def fill_subject(subject):
        browser.element("#subjectsInput").type(subject).press_enter()

    @staticmethod
    def choice_hobby():
        browser.element((By.XPATH, "//*[@for='hobbies-checkbox-2']")).click()

    @staticmethod
    def fill_address(address):
        browser.element("#currentAddress").type(address)

    @staticmethod
    def upload_image(image):
        browser.element("#uploadPicture").type(resource_path(image))

    @staticmethod
    def click_submit():
        browser.element("#submit").click()
