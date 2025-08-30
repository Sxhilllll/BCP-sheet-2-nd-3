n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(1, n+1):
    for j in range(m-i):
        print("_",end =" ")
    for k in range(i):
        print("*",end= " ")
    print()