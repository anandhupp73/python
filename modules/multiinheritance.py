#multiple inheritance

class school:
    def stexts():
        print("stext")
    def snotes():
        print("snotes")
class tution:
    def ttexts():
        print("ttexts")
    def tnotes():
        print("notes")
class students(school,tution):
    def materials():
        print("study materials")
stud=students
stud.stexts()
stud.snotes()
std1=students
std1.ttexts()


    
    