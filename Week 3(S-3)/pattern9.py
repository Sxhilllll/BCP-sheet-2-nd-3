n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    print("*" * (m-i),end=" ")
    print(" " * (2*i), end="")
    print("*" * (m-i))
