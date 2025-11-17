import os
from enum import StrEnum


class Hobbies(StrEnum):
    SPORTS = "1"
    READING = "2"
    MUSIC = "3"


class Gender(StrEnum):
    MALE = "1"
    FEMALE = "2"
    OTHER = "3"


def gender_to_string(gender: Gender) -> str:
    if gender == Gender.MALE:
        return "Male"
    elif gender == Gender.FEMALE:
        return "Female"
    else:
        return "Other"


def hobbies_to_string(hobby: Hobbies) -> str:
    if hobby == Hobbies.SPORTS:
        return "Sports"
    elif hobby == Hobbies.READING:
        return "Reading"
    else:
        return "Music"


def resource_path(file_path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
