li=[1,2,3,4,5,6,7,8,9,10,1,3,3,3]

print(f'Elements in the in list {len(li)}')
print(f'Max element in the list {max(li)}')
print(f'Min elements in the list : {min(li)}')
print(f'sum of the elements in the list : {sum(li)}')
print(f'{li.count(3)}')
print(f'{li.count(1)}')
print(f'{li.count(10)}')
print(li.index(5))

nums = [56,78,23,45]
print(nums)
nums.append(100)
print(nums)
print(f'deleted elements is : {nums.pop()}')
print(nums)
x = nums.__add__([98,45,90])
print(x)