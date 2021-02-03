def is_prime(num) -> bool:
    for i in range(2, num/2):
        if (num % i == 0):
            return False
    return True



def test_is_prime():
    assert is_prime(7)
    assert is_prime(13)
    assert not is_prime(12)


if __name__ == '__main__':
    test_is_prime()
