def get_input():
    with open("inputs/day3.txt", "r") as f:
        lines = [elt.strip() for elt in f.readlines()]
    return lines


def get_priority(letter):
    if ord(letter) >= 97:
        return ord(letter) - 96
    else:
        return ord(letter) - 38


def part1():
    lines = get_input()
    lines = [(elt[: len(elt) // 2], elt[len(elt) // 2 :]) for elt in lines]
    in_common = [set(list(elt1)).intersection(set(list(elt2))) for elt1, elt2 in lines]
    return sum([get_priority(list(elt)[0]) for elt in in_common])


def part2():
    lines = get_input()
    in_common = [
        (
            set(list(lines[i]))
            .intersection(set(list(lines[i + 1])))
            .intersection(set(list(lines[i + 2])))
        )
        for i in range(0, len(lines), 3)
    ]
    return sum([get_priority(list(elt)[0]) for elt in in_common])


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
