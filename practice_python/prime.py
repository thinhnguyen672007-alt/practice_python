def square_root_2_int(n):
    if n < 0:
        return None
    a = 0
    while (a + 1) * (a + 1) <= n:
        a += 1
    return a

def is_prime(number):
    for i in range(2, square_root_2_int(n) + 1):
        if number % i == 0:
            print("composite number")
            return
    print("prime")
            

n = int(input("Your number is:"))
is_prime(n)