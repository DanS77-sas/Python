# Write your solution here
def who_won(game_board : list):
    player_one = sum(value == 1 for row in game_board for value in row)
    player_two = sum(value == 2 for row in game_board for value in row)

    return 1 if player_one > player_two else 2 if player_two  > player_one else 0

if __name__ == "__main__":
    result = who_won(game_board)
    print(result)
