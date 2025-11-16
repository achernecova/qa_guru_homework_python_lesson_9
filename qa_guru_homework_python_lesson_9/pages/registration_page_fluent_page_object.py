from selene import be, browser, command, have
from selenium.webdriver.common.by import By

from qa_guru_homework_python_lesson_9.resourses import resource_path


class RegistrationPageFluentPageObject:

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
        return self

    def type_first_name(self, name):
        browser.element("#firstName").type(name)
        return self

    def fill_birthday(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(
            f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month"
        ).click()
        return self

    def fill_state(self, state):
        browser.element("#state").perform(command.js.scroll_into_view).click()
        browser.element("#react-select-3-input").type(state).press_enter()
        return self

    def fill_city(self, city):
        browser.element("#city").click()
        browser.element("#react-select-4-input").send_keys(city).press_enter()
        return self

    def fill_last_name(self, last_name):
        browser.element("#lastName").type(last_name)
        return self

    def fill_email(self, email):
        browser.element("#userEmail").type(email)
        return self

    def click_gender(self):
        browser.element('[for="gender-radio-2"]').should(be.clickable).click()
        return self

    def fill_number(self, number):
        browser.element("#userNumber").type(number)
        return self

    def fill_subject(self, subject):
        browser.element("#subjectsInput").type(subject).press_enter()
        return self

    def choice_hobby(self):
        browser.element((By.XPATH, "//*[@for='hobbies-checkbox-2']")).click()
        return self

    def fill_address(self, address):
        browser.element("#currentAddress").type(address)
        return self

    def upload_image(self, image):
        browser.element("#uploadPicture").type(resource_path(image))
        return self

    def click_submit(self):
        browser.element("#submit").click()
        return self

    def should_registered_user_info(
        self,
        name,
        email,
        gender,
        phone,
        birthday,
        subject,
        hobbies,
        picture,
        address,
        state_and_city,
    ):
        browser.all(".modal-content table tbody tr td:nth-child(2)").should(
            have.exact_texts(
                name,
                email,
                gender,
                phone,
                birthday,
                subject,
                hobbies,
                picture,
                address,
                state_and_city,
            )
        )
