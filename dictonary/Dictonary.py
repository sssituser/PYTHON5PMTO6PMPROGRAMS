di = dict() # {} or dict to create dictonary
print(type(di))
print(di)
print(dir(di))
di[1] = "Java"
di[2] = "Python"
di[3] =  "NET"
di[4] = "React"
di[4] = "DataScience"
di[5] = "Data Science"
print(di)
print(f'Keys in the Dictoary : {di.keys()}')
print(di.values())
# displaying the key values pairs.
for i in range(1,len(di)+1):
    print(f'{i}===>{di[i]}')
for item in di.items():
    print(item)
di[10] = "AI"
print(di)
    