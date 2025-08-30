n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
for i in range(0,n):
    for j in range(i,m):
        print("*",end=" ")
    print()