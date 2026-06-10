def area(s):
    if isinstance(s,(int)):
        print(f'Area of a square is :{s*s}')
    elif isinstance(s,(float)):
        print(f'Area of a cirlce is : {3.14*s*s}')
area(5.7)
area(6)

class PolyEx:
    def sum(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
        
        if isinstance(self.val1,(int)) and isinstance(self.val2,(int)):
            print(f'sum of {self.val1} +  {self.val2} : {self.val1+self.val2}')
        
        
        elif isinstance(self.val1,(str)) and isinstance(self.val2,(str)):
            print(f'Concatination of two strings : {self.val1+self.val2}')
p1 = PolyEx()
p1.sum(4,5)
p1.sum('kiran','kumar')
