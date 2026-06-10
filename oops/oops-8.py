class Product:
    companyname = "NIPPO"   # staic variable or class variables
    def setproduct(self,pid,pname,pcost): # pid,pname,pcost are local variable
        self.id = pid        # id name cos are instance varibles or non static variables
        self.name = pname
        self.cost = pcost
    def getproduct(self):  # nonstatic methods or instace method setproduct,getproduct
            print(f"Product Id :{self.id}\nProduct Name : {self.name}")
            print(f'Company Name : {Product.companyname}')
            
print("=========p1 object==================")
p1 = Product() # Object p1 created
p1.setproduct(112,"LBattery",50)
p1.getproduct()
print("=========p2 object=================")
p2 = Product() # Object p2 created
p2.setproduct(113,"MBattery",20)
p2.getproduct()
print("=========p3 object=================")
p3 = Product() # Object p3 created
p3.setproduct(114,"SBattery",70)
p3.getproduct()

