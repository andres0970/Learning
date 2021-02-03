import random

lives = 6

def get_word():
    possibilities = ["para", "scrap", "divi", "trip"]
    word = random.choice(possibilities)
    return word


def debug(*args):
    print(*args)


def turn_win(word, letters_guessed):
    for letter in word:
        if letter not in letters_guessed:
            return False
    return True
    # return set(word).issubset(letters_guessed)


def test_game_win():
    assert turn_win("fede", ["f", "e", "d"])
    assert turn_win("fede", ["z", "f", "e", "d"])
    assert not turn_win("fede", ["f", "e"])


def game_end(word, letters_guessed):
    if turn_win(word, letters_guessed=letters_guessed):
        print("Ganaste")
        return True
    if len(letters_guessed) > 6:
        print("Perdiste")
        return True
    return False


def test_game_end():
    assert game_end("fede", "abqwjuy")
    assert game_end("fede", "fed")
    assert not game_end("fede", "fe")


def hangman():
    word = get_word()
    letters_guessed = ""
    debug(word)
    while not game_end(word, letters_guessed=letters_guessed):
        letter = input("Ingrese su letra ")
        letters_guessed = letter + letters_guessed



if __name__ == '__main__':
    # test_game_end()
    # test_game_win()
    hangman()
