from io import StringIO

FORMAT = """
Part 1: {}
Part 2: {}
"""


def solve(in_stream: StringIO):
    start_positions = list(map(int, in_stream.read().split(",")))
    return least_cost(start_positions, linear_cost), least_cost(start_positions, triangular_cost)


def linear_cost(center, positions):
    return sum(abs(pos - center) for pos in positions)


def triangular_cost(center, positions):
    return sum((n:=abs(pos - center))*(n+1) // 2 for pos in positions)


def least_cost(start_positions: list[int], cost):
    costs = [
        (cost(center, start_positions), center)
        for center in
        range(min(start_positions), max(start_positions))
    ]
    costs.sort()
    return costs[0][0]