#hierarchical inheritance

class school:
    def classroom():
        print("class")
class staff(school):
    def notes():
        print("notes")
class students(school):
    def study():
        print("study")
std=students
std.study()
std.classroom()
std1=staff
std1.notes()
std1.classroom()