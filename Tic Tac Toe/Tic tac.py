import itertools


def win(current_game):
    # Horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} wins horizontally")

    # Diagonal
    diags = []
    for col, row, in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} wins diagonally")
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} wins diagonally")
    '''diags = []
    for col, row, in zip(list(reversed(range(len(game)))), range(len(game))):
        diags.append(game[col][row])
    print(diags)'''

    # vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} wins vertically")


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("Position occupied")
            return game_map, False

        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, False
    except IndexError as e:
        print("Please input a number between 0 and 2", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0], ]

    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player  {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? "))
            row_choice = int(input("What row do you want to play? "))
            game = game_board(game, current_player, row_choice, column_choice)
            print(game)
            if game:
                played = True


if __name__ == '__main__':
    print("hola")

# game = game_board(game, player=1, row=3, column=1)
