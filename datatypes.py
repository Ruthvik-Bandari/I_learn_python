#string type
a = "Ruthvik"
print(type(a), a)

#integer type
b = 69
print(type(b), b)

#float type
c = 0.69
print(type(c), c)

#Complex type (denoted with letter "j" as i is used in loops)
d = 5j
print(type(d), d)

#list type
e = ["Apple", "Samsung", "Google Pixel"]
print(type(e), e)

#tuple type
f = {"bmw", "Porsche", "Benz"}
print(type(f), f)

#Dictionary type
my_dict = {"Name": "Bandari Ruthvik Nath", "Age": 21, "Nationality": "Indian"}
print(my_dict["Name"])
my_dict["Age"] = 22    #modify a value
my_dict["Sex"] = "Male" #New key value pair
print(type(my_dict), my_dict)

#set type
"""
consist of mutable sets values
"""
g = {1,2,3}
#adding a element (modifying the set)
g.add (4)
#removing the element
g.remove (1)
print(type(g), g)

"""
frozenset type
this set is a immutable varient of sets
this is used for storing values which shall not need any modification in the future
trying to add, delete or replace shall show error
operations can be performed using these frozen sets and repetations are removed in these.
"""
h = frozenset([1,2,3,4])
i = frozenset([3,4,5,6])
#performing subtraction using "-" operator
difference = h - i
print (type(difference), difference)
difference = i - h
print (difference)
#difference using the .difference()method
difference_method=h.difference(i)

#boolean type
i = "True"
if i:
    print("i is True")

#bytes type. This convert string into bits
j = b"Ruthvik"
print(type(j), j)

#bytearray is a mutable varient of bytes
k = bytearray(5)
print(k)
k[0] = 100
print(type(k),k)

#memory view, this helps in viewing the memory without copying instead
l = memoryview(bytes(5))
print(type(l), l)
# Accessing the first byte of the memory
print(l[0])

#NoneType
m = None
if m is None:
    print(type(m), "m is None")

