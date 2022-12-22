# 123 - > 1**3 + 2**3 + 3**3

user_input = 123
temp = user_input

size = len(str(user_input))
sum = 0

while temp!=0:
    digit = temp%10
    sum = sum + digit**size
    temp = temp//10


if user_input == sum:
    print("This number is an Armstrong Number - ", sum)
else:
    print("Your Number is not an Armstrong Number - ",sum)