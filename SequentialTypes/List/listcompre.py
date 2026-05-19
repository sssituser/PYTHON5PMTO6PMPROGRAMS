li = [1,2,3,3,3,4,5,6,77,7,7,7,8]
print(li)
evenlist =[x for x in li if x%2==0]
print(evenlist)

oddlist = [x for x in li if x%2!=0]
print(oddlist)

threelist =[x for x in li if x%3==0]
print(threelist)

mutiplesoftwo =[2*x for x in li]
print(mutiplesoftwo)