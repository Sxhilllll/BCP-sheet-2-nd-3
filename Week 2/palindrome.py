A=int(input("Enter a number: "))

#initialise original num with A
original = A

reverse_num = 0
while A > 0:
    digit = A % 10
    reverse_num = reverse_num * 10 + digit
    A = A//10

#check palindrome
if original == reverse_num:
    print("Yes it is a palindrome")
else:
    print("No not a palindrome")