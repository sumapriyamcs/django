
n = int(input("Enter no of  recors"))
rcd=[]
rcdlst=[]
rslt=[]
for i in range(n):
     names=input("Enter the name")
     score=float(input("Enter the score "))
     rcd+=[[names,score]]
    # print(rcd)
     rcdlst += [score]
     rslt = max(list(rcdlst))

print(rslt)
l=[]


for i,j in sorted(rcd):
    if j == rslt:
        l.append(i)
for i in l:
    print(i)


data = [['b', 10], ['Shyama', 20], ['Rama', 20]]

names = []
marks = []

for i, j in data:
    names.append(i)
    marks.append(j)

max_marks = max(marks)

list1 = []

for i, j in data:
    if j == max_marks:
        list1.append(i)

print(sorted(list1))

data = [['b', 10], ['ram', 20], ['cgh', 20]]

names = []
marks = []
dict1 = {}

for i, j in data:
    dict1[i] = j
dict2={}
for i, j in dict1.items():
    value = max(dict1.values())
    if j == value:
        #dict2=value
        print(i)




