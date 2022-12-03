def get_input():
    with open("inputs/day2.txt", "r") as f:
        lines = [elt.strip().split(" ") for elt in f.readlines()]
    return lines


def get_score(opponent_move, my_move):
    if my_move == "X":
        score = 1
    elif my_move == "Y":
        score = 2
    else:
        score = 3

    if (
        (opponent_move == "C" and my_move == "X")
        or (opponent_move == "B" and my_move == "Z")
        or (opponent_move == "A" and my_move == "Y")
    ):
        # win
        score += 6
    elif ord(opponent_move) == (ord(my_move) - 23):
        # draw
        score += 3
    return score


def get_move(opponent_move, outcome):
    if outcome == "X":
        # need to loose
        if opponent_move == "A":
            move = "Z"
        elif opponent_move == "B":
            move = "X"
        else:
            move = "Y"
    elif outcome == "Y":
        # draw
        move = chr(ord(opponent_move) + 23)
    else:
        if opponent_move == "A":
            move = "Y"
        elif opponent_move == "B":
            move = "Z"
        else:
            move = "X"
    return opponent_move, move


def part1():
    rounds = get_input()
    return sum([get_score(*r) for r in rounds])


def part2():
    rounds = get_input()
    return sum([get_score(*get_move(*r)) for r in rounds])


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
