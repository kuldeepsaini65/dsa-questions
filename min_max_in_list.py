numbers = [0,1,34,56,100,34,-1,56,34,67]
max = 0
min = numbers[1]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]

    if numbers[i]<min:
        min = numbers[i]

print("Maximum Number in list is - " ,max)
print("Minimum Number in list is - " ,min)