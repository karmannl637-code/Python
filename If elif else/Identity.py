a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# c=a/a=c b=a 
print(a is c, id(a), id(c))
print(a is b, id(a), id(b))
print(a is not c, id(a), id(c))
print(a is not b, id(a), id(b))