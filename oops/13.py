import math
class Calcy:
    def sum(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(f'sum is :{self.num1+self.num2}')
    def sub(self):
        print(f'sub is : {self.num1-self.num2}')
        
    def mul(self):
        print(f'mul is : {self.num1*self.num2}')
        
    def div(self):
        print(f'div is : {self.num1/self.num2}')
        
class SciCalcy(Calcy):
    def sin(self,val):
        print(f'Sin {val} is {math.sin(val)}')
    def cos(self,val):
        print(f'cos {val} is {math.cos(val)}')
s1 = SciCalcy()
s1.sin(90)
s1.cos(0)
s1.sum(5,2)
s1.sub()
s1.mul()
s1.div()