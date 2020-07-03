def is_prime(n):
    isPrime=False
    for i in range(2,n):
        if n % i ==0:
            isPrime=False
            break
        else:
            isPrime=True
    return isPrime


print(is_prime(2))
print(is_prime(4))
print(is_prime(11))
print(is_prime(99))
print(is_prime(23))
