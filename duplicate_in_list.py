a = [10,20,10,30,40,90,80,67,20]
duplicate = []
double = []
for i in range(len(a)):
    if a[i] not in duplicate:
        duplicate.append(a[i])
    
    elif a[i] in duplicate:
        double.append(a[i])

print(a)
print("Duplicate Numbers Are - ",double)