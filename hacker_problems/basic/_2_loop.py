"""
Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i2 .

"""
n = int(input("Enter integer no : "))
for i in range(n):
    result = i ** 2
    print(result)