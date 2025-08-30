n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    print("*" * (m-i),end=" ")
    print(" " * (2*i), end="")
    print("*" * (m-i))

for i in range(1,n+1):
    print("*" * i,end=" ")
    print(" " * (2*(n - i)),end="")
    print("*" * i)