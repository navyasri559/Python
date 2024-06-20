r = int(input("Enter number of rows"))
c = int(input("Enter number of columns"))
a = []
for i in range(r) :
    x = []
    for j in range(c) :
        x.append(int(input("enter elements")))
    a.append(x)
print("Matrix is")
for i in range(r) :
    for j in range(c) :
              print(a[i][j],end=" ")
    print()
r1 = int(input("Enter number of rows"))
c1= int(input("Enter number of columns"))
b = []
for i in range(r1) :
    x = []
    for j in range(c1) :
        x.append(int(input("enter elements")))
    b.append(x)
print("Matrix is")
for i in range(r1) :
    for j in range(c1) :
              print(b[i][j],end=" ")
    print()
c = []
for i in range(len(a)):
    for j in range(len(a[0])):
     c[i][j]=a[i][j]+b[i][j]