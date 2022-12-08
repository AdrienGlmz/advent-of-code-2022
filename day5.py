def get_input():
    with open("inputs/day5.txt", "r") as f:
        lines = [elt for elt in f.readlines()]
    end_of_setup_idx = lines.index("\n")
    setup, moves = lines[:end_of_setup_idx], lines[(end_of_setup_idx + 1) :]

    # Transpose setup to create stacks
    setup = list(zip(*[list(elt[:-1]) for elt in setup]))
    # Keep only stack identified by a number
    setup = {
        int(elt[-1]): [e for e in elt[:-1] if e != " "][::-1]
        for elt in setup
        if 49 <= ord(elt[-1]) <= 57
    }
    return setup, moves


class Supplies:
    def __init__(self, initial_setup, moves):
        self.stacks: dict[list] = initial_setup
        self.moves: list = moves

    def move(self, rep, start, end):
        for _ in range(rep):
            self.stacks[end].append(self.stacks[start].pop(-1))

    def move_v2(self, nb, start, end):
        self.stacks[end].extend(self.stacks[start][-nb:])
        self.stacks[start] = self.stacks[start][:-nb]

    def run(self, how, nb_steps=None):
        if nb_steps:
            self.moves = self.moves[:nb_steps]
        for m in self.moves:
            _, rep, _, start, _, end = m.split(" ")
            how(int(rep), int(start), int(end))


def part1():
    s, m = get_input()
    supplies = Supplies(s, m)
    supplies.run(how=supplies.move)
    return "".join([elt[-1] for elt in list(supplies.stacks.values())])


def part2():
    s, m = get_input()
    supplies = Supplies(s, m)
    supplies.run(how=supplies.move_v2)
    return "".join([elt[-1] for elt in list(supplies.stacks.values())])


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
