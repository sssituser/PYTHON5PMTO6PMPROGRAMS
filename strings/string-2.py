s = "abc"
print(s.__getitem__(0))
print(s.__getitem__(1))

dob = "10-Oct-2025"
res = dob.split('-')
print(res)
print(res[0])
print(res[1])
print(res[2])
print("==================================")
print(s) # abc
x = s.replace('a','z')
print(s) # zbc
print(x)