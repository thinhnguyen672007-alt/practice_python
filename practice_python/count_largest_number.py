number = list(map(int, input(). split()))
n = len(number)
count = 1
for i in range(0,n):
    for j in range(i+1,n):
        if number[i] > number[j]:
            tmp = number[i]
            number[i] = number[j]
            number[j] = tmp
for largest_appear in range(n-1, 0, -1):
    if number[largest_appear] == number[largest_appear-1]:
        count +=1
    else:
        break
print(number)
print(count)
            
    
