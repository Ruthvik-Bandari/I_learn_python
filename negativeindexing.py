"""
Here we use negative index to start the slicing from the end of the string.
Question:
In the word "Hello, World! from o in world (position = -5) to, but not included :"d" in the world (position = -2) 

H   E   L   L   O   ,      W   O   R   L   D   !
0   1   2   3   4   5  6   7   8   9   10  11  12
-13 -12 -11 -10 -9 -8 -7  -6  -5  -4   -3  -2  -1
"""
a = "Hello, World!"
print(a[-5:-2])