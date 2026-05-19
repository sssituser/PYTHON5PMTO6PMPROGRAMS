t = (10,39,56,78,90)
print(t[0],t[-5])

print("Displaying the elements using for loop")
for element in t:
    print(element)
    
print("Displaying the elements using +ve index")
for index in range(len(t)):
    print(f't[{index}]   {t[index]}')
    
print("Displaying the elements using -ve index")
for index in range(-1,-(len(t)+1),-1):
    print(f't[{index}]   {t[index]}')
    
    
print("Displaying the elements using -ve index")
for index in range(-5,0,1):
    print(f't[{index}]  {t[index]}')