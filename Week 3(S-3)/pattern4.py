n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
for i in range(1,n+1):
     num = 1
     for j in range(1,i+1):
          if j % 2 == 1:
               print(num, end=" ")
               num = num+2
          else:
               print("*", end =" ")
     print()
 