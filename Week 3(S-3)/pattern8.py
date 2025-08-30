n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    for j in range(i):
        print("_",end=" ")
    for k in range(m-i):
        print("*",end=" ")
    print()