"""
The provided code stub read in a dictionary containing key/value pairs of name:[Marks] for a
list of students. Print the average of the marks array for the student name provided, showing
2 places after the decimal.

"""
'''
s_no=int(input("Enter the no of student"))
dict1 = {}
mk=[]

mk1=[]

for i in range(1,s_no+1):
    name=input("enter the name of student : ")
    dict1[name.title()] = mk

    for i in range(3):
       marks=float(input("Enter marks of student : "))
       for j in marks:
         mk.append(j)

    print(dict1)
'''
n = int(input("Enter total no of student : "))
student_marks = {}
for _ in range(n):
  name, *line = input("Enter name : ").split()
  scores = list(map(float, line))
  student_marks[name] = scores
  query_name = input("query name")
output = list(student_marks[query_name])
per = sum(output)/len(output);
print("%.2f" % per);