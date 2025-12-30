n = int(input())
for j in range(n):
    n, k = map(int, input().split())
    space = list(map(int,input().split()))[:n]
    max_plant = 0
    for i in range(n):
        if space[i] == 0:
            can_plant = True
            if i > 0 and space[i-1] == 1:
                can_plant = False
            if i < n-1 and space[i+1] == 1:
                can_plant = False
            if can_plant == True:
                space[i] = 1
                max_plant +=1
    if max_plant >= k:
        print("true")
    else: 
        print("false")
    
