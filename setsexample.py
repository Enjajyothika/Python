

a={1,2,3,4,5}
b={2,3,6,7,8}
print(a.union(b),a,b)
print(len(a))
print(a.update(b),a)#updates and makes changes in a set 
print(a|b)#union
a={1,2,3,4,5}
b={2,34,5,7,8}
print(a.intersection(b),a,b)
print(a.intersection_update(b),a,b)#updates and makes changes in a set 
print(a&b)
a={1,2,3,4,5}
b={2,34,6,7,8}
print(a.difference(b),a,b)
print(a.difference_update(b),a,b)#updates and makes changes in a set 
print(a-b)#difference