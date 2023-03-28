# if u dont want '\'special
print(r'C:\some\name')

# 有沒有\差在有沒有忽略換行
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 負號index
word = 'Python'
print(word[-1])

"""
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

# list可包含list
# a = ['a', 'b', 'c']
n = [1, 2, 3]
# x = [a, n]
# print(x)

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

