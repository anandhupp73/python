#multilevel inheritance
class school:
    def teachers():
        print("teachers")
class classroom(school):
    def notes():
        print("notes")
class student(classroom):
    def study():
        print("study")
std=student
std.teachers()
std.notes()
std.study()
