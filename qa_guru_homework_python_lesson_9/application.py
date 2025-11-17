from selene import browser

from qa_guru_homework_python_lesson_9.pages.left_panel_element import LeftPanelElement
from qa_guru_homework_python_lesson_9.pages.simple_page import SimplePage


class Application:
    def __init__(self):
        self.left_panel = LeftPanelElement()
        self.simple_page = SimplePage()

    def open(self):
        browser.open("/")
        return self


app = Application()
