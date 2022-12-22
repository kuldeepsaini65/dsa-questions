# 121 -->  121

user_number = 121

reverse = 0
temp = user_number
while temp!=0:
    reverse = (reverse*10) + temp%10
    temp  = temp//10
    
if user_number == reverse:
    print("Yes it is a pelendrome number")
else :
    print("not a pelendrome number")