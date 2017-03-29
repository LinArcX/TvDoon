class Student(object):
    name = ""
    age = 0
    major = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major


def make_student(name, age, major):
    student = Student(name, age, major)
    return student

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\e[3m'
    END = '\033[0m'