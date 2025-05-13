import argparse
import numpy as np
import matplotlib.pyplot as plt

from lib.annealers.tsp_annealer import TSPAnnealer
from Lab06.pagerank import DirectedGraph, PageRank


def task1() -> None:
    nodes = {
        "A": ["E", "F", "I"],
        "B": ["A", "C", "F"],
        "C": ["B", "D", "E", "L"],
        "D": ["C", "E", "H", "I", "K"],
        "E": ["C", "G", "H", "I"],
        "F": ["B", "G"],
        "G": ["E", "F", "H"],
        "H": ["D", "G", "I", "L"],
        "I": ["D", "E", "H", "J"],
        "J": ["I"],
        "K": ["D", "I"],
        "L": ["A", "H"],
    }

    name_to_id = {name: i for i, name in enumerate(sorted(nodes))}
    id_to_name = {i: name for name, i in name_to_id.items()}

    graph = DirectedGraph()
    for src, destinations in nodes.items():
        for destination in destinations:
            graph.add_edge(name_to_id[src], name_to_id[destination])

    pr = PageRank(graph)
    print("=== Random Walk ===")

    rw_result = pr.random_walk()
    for node, score in sorted(rw_result.items(), key=lambda x: x[1], reverse=True):
        print(f"{id_to_name[node]}: {score:.6f}")

    print("\n=== Power Iteration ===")
    pi_result = pr.power_iteration()
    for node, score in sorted(pi_result.items(), key=lambda x: x[1], reverse=True):
        print(f"{id_to_name[node]}: {score:.6f}")


def task2(input_file: str) -> None:
    coords = np.loadtxt(input_file, dtype=int)

    def beta_function(iteration: int, max_iterations: int) -> float:
        min_beta = 0.01
        max_beta = 10
        p = 3
        return min_beta + (max_beta - min_beta) * (iteration / max_iterations) ** p

    annealer = TSPAnnealer(
        coords=coords,
        beta_function=beta_function,
        max_iterations=200_000,
        solution_memory=False,
        cost_memory=True,
        beta_memory=True,
        p_accept_memory=True,
    )

    solution, cost = annealer.anneal()
    solution_coords = coords[solution]

    print(f"Final order: {solution}")
    print(f"Final distance: {cost}")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    x = np.append(solution_coords[:, 0], solution_coords[0, 0])
    y = np.append(solution_coords[:, 1], solution_coords[0, 1])

    axes.flat[0].plot(x, y, marker="o", linestyle="-")
    axes.flat[0].set_title("Final Solution")
    axes.flat[0].set_xlabel("X")
    axes.flat[0].set_ylabel("Y")
    axes.flat[0].set_aspect("equal")

    axes.flat[1].plot(annealer.cost_history)
    axes.flat[1].set_title("Distance History")
    axes.flat[1].set_xlabel("Iteration")
    axes.flat[1].set_ylabel("Distance")

    axes.flat[2].plot(annealer.beta_history)
    axes.flat[2].set_title("Beta History")
    axes.flat[2].set_xlabel("Iteration")
    axes.flat[2].set_ylabel("Beta")

    axes.flat[3].plot(annealer.p_accept_history, ",")
    axes.flat[3].set_title("Acceptance Probability History")
    axes.flat[3].set_xlabel("Iteration")
    axes.flat[3].set_ylabel("Acceptance Probability")

    plt.tight_layout()
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(description="Grafy-Lab06")
    parser.add_argument(
        "-t", "--task", type=int, required=True, help="Select Task (1, 2)"
    )
    parser.add_argument("-i", "--input", type=str, help="Input file")
    args = parser.parse_args()

    if args.task == 1:
        task1()
    elif args.task == 2:
        if not args.input:
            print("Error: Input file required for task 2")
            return
        task2(args.input)
    else:
        print("Invalid task selected.")


if __name__ == "__main__":
    main()
