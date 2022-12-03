def get_input():
    with open('inputs/day1.txt', 'r') as f:
        lines = ''.join(f.readlines())
    return lines


def part1():
    lines = get_input()
    calories = [sum([int(e) if e else 0 for e in elt.split('\n')]) for elt in lines.split('\n\n')]
    return max(calories)


def part2():
    lines = get_input()
    calories = [sum([int(e) if e else 0 for e in elt.split('\n')]) for elt in lines.split('\n\n')]
    return sum(sorted(calories, reverse=True)[:3])


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
