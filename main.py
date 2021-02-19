def fibonnaci(number):
    if number == 0:
        print (1)
    else:
        a = 0
        b = 1
        for i in range(1, number):
            c = a + b
            a = b
            b = c
        return b


def user_inter ():
    num = int(input("Cuantos numeros de la serie "))
    result = fibonnaci(num)
    print(result)

def test_fibonnaci():
    assert fibonnaci(9) == 34
    assert fibonnaci(1) == 1
    assert fibonnaci(2) == 1


if __name__ == '__main__':
    test_fibonnaci()