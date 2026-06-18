class A:
    def hi(self):
        print(f'Hi Method from cLass A')
class B:
    def bye(self):
        print("Hi this bye method Clas B")
class C:
    def show(self):
        print("Hi this is show method from class C")
class D(A,B,C):
    def display(self):
        print("Hi this is display method from class D")
d =  D()
d.hi()
d.bye()
d.show()
d.display()