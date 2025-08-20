N = int(input("Enter N: "))
count = 0

for digit in str(N):   # convert to string, loop over each digit
    count += 1

print("Count of digits =", count)