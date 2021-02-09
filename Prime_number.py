def is_prime(num) -> bool:
    for i in range(2, num // 2):
        if (num % i == 0):
            #print("No es primo")
            return False
    #print("Es primo")
    return True

def all_primes (num):
    prime_numbers = []
    for i in range(2, num):
        if is_prime(i):
            prime_numbers.append(i)
    print(prime_numbers)



def test_is_prime():
    assert is_prime(7)
    assert is_prime(13)
    assert not is_prime(12)


if __name__ == '__main__':
    all_primes(17)
