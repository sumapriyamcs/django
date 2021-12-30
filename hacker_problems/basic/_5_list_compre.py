"""
Problem
Let’s learn about list comprehensions! You are given three integers x, y and z representing the dimensions
of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D
grid where the sum of i + j + k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Please use
list comprehensions rather than multiple loops, as a learning exercise.

Example

x = 1
y = 1
z = 2
n = 3

All permutations of [i, j, k] are:
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]].

Print an array of the elements that do not sum to n = 3.
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1],  [1, 1, 0],  [1, 1, 2]]

"""
x = int(input("Enter the no"))
y = int(input("Enter the no"))
z = int(input("Enter the no"))
n = int(input("Enter the no"))
lst = []
for x in range(x+1):
    for y in range(y+1):
        for z in range(z+1):
            if x+y+z != n:
                rst= [x,y,z]
                print(rst)
                lst.append(rst)
print(lst)

rst = ([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k !=n])
print("Using list comprehension", rst)




