from abc import ABC, abstractmethod
import random
from typing import Tuple


class Annealer(ABC):
    def __init__(
        self,
        initial_solution,
        max_iterations,
        solution_memory=False,
        cost_memory=False,
        beta_memory=False,
        p_accept_memory=False,
    ):
        self.initial_solution = initial_solution
        self.max_iterations = max_iterations
        self.solution_memory = solution_memory
        self.cost_memory = cost_memory
        self.beta_memory = beta_memory
        self.p_accept_memory = p_accept_memory

        self.reset()

    @abstractmethod
    def propose_solution(self) -> Tuple[any, float | None]:
        pass

    @abstractmethod
    def cost_function(self, solution) -> float:
        pass

    @abstractmethod
    def p_accept(self, new_cost) -> float:
        pass

    @abstractmethod
    def beta(self) -> float:
        pass

    def log_results(self):
        if self.solution_memory:
            self.solution_history.append(self.solution)
        if self.cost_memory:
            self.cost_history.append(self.cost)
        if self.beta_memory:
            self.beta_history.append(self.beta())

    def reset(self):
        self.solution = self.initial_solution
        self.cost = self.cost_function(self.initial_solution)
        self.iteration = 0

        self.solution_history = []
        self.cost_history = []
        self.beta_history = []
        self.p_accept_history = []

        self.log_results()

    def anneal_step(self):
        if self.iteration >= self.max_iterations:
            return False

        new_solution, new_cost = self.propose_solution()

        if new_cost is None:
            new_cost = self.cost_function(new_solution)

        p_acc = self.p_accept(new_cost)

        if random.random() <= p_acc:
            self.solution = new_solution
            self.cost = new_cost

        self.log_results()

        if self.p_accept_memory:
            self.p_accept_history.append(p_acc)

        self.iteration += 1

        return True

    def anneal(self, num_steps=None):
        if num_steps is None:
            num_steps = self.max_iterations

        for _ in range(num_steps):
            if not self.anneal_step():
                break

        return self.solution, self.cost
