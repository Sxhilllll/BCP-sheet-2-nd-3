n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
for i in range(n):
    for j in range(m):
        if j == 0 or j == n - 1:   
            print("*", end=" ")
        else:                        
            print("_", end=" ")
    print()