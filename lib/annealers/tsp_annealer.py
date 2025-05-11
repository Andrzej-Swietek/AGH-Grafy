from lib.annealers.annealer import Annealer

from math import sqrt, exp
from itertools import combinations
import random


class TSPAnnealer(Annealer):
    def __init__(
        self,
        coords,
        beta_function,
        max_iterations,
        solution_memory=False,
        cost_memory=True,
    ):
        self.num_cities = len(coords)
        self.coords = coords
        self.beta_function = beta_function
        self.distances = [
            sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)
            for u, v in combinations(coords, 2)
        ]

        super().__init__(
            initial_solution=list(range(self.num_cities)),
            max_iterations=max_iterations,
            solution_memory=solution_memory,
            cost_memory=cost_memory,
        )

    def dist(self, i, j):
        if i == j:
            return 0
        else:
            i, j = sorted([i, j])
            return self.distances[(2 * self.num_cities - 1 - i) * i // 2 + j - i - 1]

    def propose_solution(self):
        # 2-opt swap
        i = random.randint(0, self.num_cities - 2)
        j = i + 1

        if i < 2:
            k = random.randint(j + 1, self.num_cities - 2)
        elif j > self.num_cities - 3:
            k = random.randint(0, i - 2)
        else:
            k = random.choice([n for n in range(self.num_cities) if n not in (i, j)])

        l = k + 1

        _, start, end, _ = sorted([i, j, k, l])

        new_solution = self.solution[:]

        while start < end:
            new_solution[start], new_solution[end] = (
                new_solution[end],
                new_solution[start],
            )
            start += 1
            end -= 1

        return new_solution

    def cost_function(self, solution):
        return sum(
            self.dist(solution[i - 1], solution[i]) for i in range(self.num_cities)
        )

    def p_accept(self, new_cost):
        if new_cost < self.cost:
            return 1
        return exp((self.cost - new_cost) * self.beta())

    def beta(self):
        return self.beta_function(self.iteration, self.max_iterations)
