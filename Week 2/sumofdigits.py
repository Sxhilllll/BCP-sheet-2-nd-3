N = int(input("Enter N: "))
total = 0

for digit in str(N):   # loop through each digit (string way)
    total += int(digit)

print("Sum of digits =", total)
