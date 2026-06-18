class A:
    def readnums(self,a,b):
        self.a = a
        self.b = b
    def shownums(self):
        print(f'a = {self.a}  b = {self.b}')
class B(A):
    def sum(self):
        print(f'sum is :{self.a+self.b}')
    def sub(self):
        print(f'sub is :{self.a-self.b}')
class C(B):
    def mul(self):
        print(f'mul is :{self.a*self.b}')
    def div(self):
        print(f'div is :{self.a/self.b}')
p = C()
p.readnums(5,2)
p.shownums()
p.sum()
p.sub()
p.mul()
p.div()