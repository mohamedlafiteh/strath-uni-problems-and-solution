
import random


def get_random():
    return random.randint(1, 6)


def snake_function(actions):
    player_position = 0
    number_roles = 0

    while True:
        player_position += get_random()
        number_roles += 1
        if player_position >= 100:
            break
        if player_position in actions.keys():
            player_position = actions[player_position]

    return number_roles


if __name__ == "__main__":
    actions = {}
    actions[4] = 14
    actions[9] = 31
    actions[17] = 7
    actions[20] = 38
    actions[28] = 84
    actions[40] = 59
    actions[51] = 67
    actions[54] = 34
    actions[62] = 19
    actions[64] = 60
    actions[71] = 91
    actions[87] = 24
    actions[93] = 73
    actions[95] = 75
    actions[99] = 78

    snake = snake_function(actions)
    print(snake)
