import os


def resource_path(file_path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
