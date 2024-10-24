#represents true or false values
x = "hello"
y = 15
print (bool(x), bool(y))

#to return false 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
class myclass ():
    def __len__(self):
        return 0
myobj = myclass ()
print(bool(myobj))

#to return true value
def myfunction():
    return True
if myfunction():
    print("Yes!")
else:
    print("No!")

#using built-in function isinstance()
x = 200
print(isinstance(x, int))