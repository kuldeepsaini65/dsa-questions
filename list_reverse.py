# Python Program to reverse a list 

ar = [1,2,3,4,5,6,7,8,9,10]
left = 0
right = len(ar)-1

while left<right:
    temp =ar[left]
    ar[left] = ar[right]
    ar[right] = temp 

    left +=1
    right -=1

print(ar)

