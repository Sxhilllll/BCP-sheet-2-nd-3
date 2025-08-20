
A = int(input("Enter value of A: "))
B = int(input("Enter value of B: "))

result = 1  #initialising the result var with 1
for i in range(B):
    result *= A

print("Result:", result)
