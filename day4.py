def get_input():
    with open("inputs/day4.txt", "r") as f:
        lines = [elt.strip().split(",") for elt in f.readlines()]
    sections = [(elt1.split("-"), elt2.split("-")) for elt1, elt2 in lines]
    sets = [
        (set(range(int(l1[0]), int(l1[1]) + 1)), set(range(int(l2[0]), int(l2[1]) + 1)))
        for l1, l2 in sections
    ]
    return sets


def part1():
    return sum([s1.issubset(s2) or s2.issubset(s1) for s1, s2 in get_input()])


def part2():
    return sum([len(s1.intersection(s2)) > 0 for s1, s2 in get_input()])


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
