#parameterised constructor
class synnefo:
    def __init__(self,branch):
        self.name=input("enter name")
        self.age=int(input("enter age"))
        self.branch=branch
    def python(self):
        print("python",self.name,self.age,self.branch)
std=synnefo("ekm")
std.python()
std2=synnefo("clt")
std2.python()