from abc import ABC, abstractmethod
import random


class Annealer(ABC):
    def __init__(
        self, initial_solution, max_iterations, solution_memory=False, cost_memory=True
    ):
        self.initial_solution = initial_solution
        self.solution_memory = solution_memory
        self.cost_memory = cost_memory
        self.max_iterations = max_iterations

        self.reset()

    @abstractmethod
    def propose_solution(self):
        pass

    @abstractmethod
    def cost_function(self, solution):
        pass

    @abstractmethod
    def p_accept(self, new_cost):
        pass

    @abstractmethod
    def beta(self):
        pass

    def log_results(self):
        if self.solution_memory:
            self.solution_history.append(self.solution)
        if self.cost_memory:
            self.cost_history.append(self.cost)

    def reset(self):
        self.solution = self.initial_solution
        self.cost = self.cost_function(self.initial_solution)
        self.iteration = 0

        self.solution_history = []
        self.cost_history = []
        self.beta_history = []

        self.log_results()

    def anneal_step(self):
        if self.iteration >= self.max_iterations:
            return False

        new_solution = self.propose_solution()
        new_cost = self.cost_function(new_solution)

        if random.random() <= self.p_accept(new_cost):
            self.solution = new_solution
            self.cost = new_cost

        self.log_results()

        self.iteration += 1

        return True

    def anneal(self, num_steps=None):
        if num_steps is None:
            num_steps = self.max_iterations

        for _ in range(num_steps):
            if not self.anneal_step():
                break

        return self.solution, self.cost
