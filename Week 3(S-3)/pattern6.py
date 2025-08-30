n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    print("*",end=" ")
    for j in range(m-i):
        print("_",end=" ")
    print("*")
