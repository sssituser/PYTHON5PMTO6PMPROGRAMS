li = [6,89.7,6+7j,'abc',True,[78,79],6,89.7]
print(type(li))
print(li)

print("Printing the elements using +ve index")
print(li[0],li[1],li[2],li[3],li[4],li[5],li[6])

print("Printing the elements using -ve index")
print(li[-1],li[-2],li[-3],li[-4],li[-5],li[-6],li[-7])

print("Diplaying the elments in the list using for loop")
print(f"Total elements present in the list : {len(li)}")

print("Displaying the elements using loop +ve index")
for i in range(0,len(li)):
    print(f'li[{i}]=>{li[i]}',end=" ")
    
print("Displaying the elements using loop -ve index")
for i in range(-1,-(len(li)+1),-1):
    print(f'li[{i}]=>{li[i]}',end=" ")

