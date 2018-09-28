def is_prime(num):
    for i in range(2,num):
        if(num % i == 0):
            return 0
    return 1

def is_even(num):
    if(num % 2 == 0):
        return 1
    else:
        return 0