n = int(input())
numbers = list(map(int, input().split()))[:n]
length = len(numbers)
lowest_number = numbers[0]
mutiple = 1
for i in range(length):
    if lowest_number > numbers[i]:
        lowest_number = numbers[i]
for j in range(length):
    if numbers[j] == lowest_number:
        mutiple *= ( lowest_number + 1 )
    if numbers[j] == numbers[j]:
        mutiple *= numbers[j]
print(mutiple)        
        
    
    