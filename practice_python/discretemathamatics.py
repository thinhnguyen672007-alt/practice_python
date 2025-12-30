def square_root_2_int(n) :
    if n < 0:
        return None
    a = 0
    while (a + 1) * (a + 1) <= n :
        a += 1
    return a

def is_prime(number) :
    check = 0
    if number < 2:
        print("NO")
        exit()
    for i in range(2, square_root_2_int(number) + 1) :
        check = 0
        if number % i == 0 :
            print("NO")
            exit()
    if check == 0:
        return number
    
numbers = int(input())
index_numbers = [int(d) for d in str(numbers)]
length = len(index_numbers)
total_even_position = 0
for i in range(length) :
    if i % 2 != 0 :
        if is_prime(index_numbers[i]) :
            total_even_position += index_numbers[i]
if is_prime(total_even_position) :
    print("YES")
                
            