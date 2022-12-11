from itertools import permutations


def get_input():
    with open("inputs/day6.txt", "r") as f:
        lines = f.readline().strip()
    return lines


def different_characters(li):
    return all([a != b for a, b in permutations(li, r=2)])


def get_start_packet_marker(buffer, nb):
    i = 0
    while not different_characters(buffer[i : i + nb]):
        i += 1
    return i + nb


def part1():
    buffer = get_input()
    return get_start_packet_marker(buffer, nb=4)


def part2():
    buffer = get_input()
    return get_start_packet_marker(buffer, nb=14)


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
