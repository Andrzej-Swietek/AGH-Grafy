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
        cost_memory=False,
        beta_memory=False,
        p_accept_memory=False,
    ):
        self.num_cities = len(coords)
        if self.num_cities < 4:
            raise ValueError("Number of cities must be at least 4.")
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
            beta_memory=beta_memory,
            p_accept_memory=p_accept_memory,
        )

    def dist(self, i, j):
        if i == j:
            return 0
        else:
            i, j = sorted([i, j])
            return self.distances[(2 * self.num_cities - 1 - i) * i // 2 + j - i - 1]

    def propose_solution(self):
        # 2-opt swap (a, b) and (c, d) -> (a, c) and (b, d)
        a = random.randint(-self.num_cities, -1)
        b = a + 1
        c = random.randint(b + 1, a + self.num_cities - 2)
        d = c + 1

        new_solution = self.solution[:]
        new_cost = (
            self.cost
            - self.dist(new_solution[a], new_solution[b])
            - self.dist(new_solution[c], new_solution[d])
            + self.dist(new_solution[a], new_solution[c])
            + self.dist(new_solution[b], new_solution[d])
        )

        while b < c:
            (
                new_solution[b],
                new_solution[c],
            ) = (
                new_solution[c],
                new_solution[b],
            )
            b += 1
            c -= 1

        return new_solution, new_cost

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
