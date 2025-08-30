# n = int(input("Enter the number of stars"))
# for i in range(1,n+1):
#     print("*",end=" ")

n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
for i in range(0,n):
    for  j in range(0,m):
        print("*",end=" ")
    print()
    