s = {1,2,3,4,5,}
print(s)
print(f'Total elements in the set are : {len(s)}')
print(f'Max element in the set is : {max(s)}')
print(f'Max element in the set is : {min(s)}')
print(f'sum of the elements :{sum(s)}')
s.clear()
print(s)

p = {1,2,3,4,5,6,7} 
q = {3,4,5,6,8,9}
r = p.union(q)
s = p.intersection(q)
print(f'p = {p}')
print(f'q = {q}')
print(f'r = {r}')
print(f's = {s}')
d1 = p-q
print(f'difference d1 = {d1}')
d2 = q-p
print(f'difference d2 = {d2}')
d3 = p.symmetric_difference(q)
print(f'd3 = {d3}')
