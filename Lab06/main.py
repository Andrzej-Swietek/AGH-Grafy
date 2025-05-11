import argparse
import numpy as np
import matplotlib.pyplot as plt

from lib.annealers.tsp_annealer import TSPAnnealer


def task2(input_file: str) -> None:
    coords = np.loadtxt(input_file, dtype=int)

    def beta_function(iteration: int, max_iterations: int) -> float:
        min_beta = 0.01
        max_beta = 300
        p = 3
        return min_beta + (max_beta - min_beta) * (iteration / max_iterations) ** p

    annealer = TSPAnnealer(
        coords=coords, beta_function=beta_function, max_iterations=100000
    )

    solution, cost = annealer.anneal()
    solution_coords = coords[solution]

    print(f"Final order: {solution}")
    print(f"Final distance: {cost}")

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    x = np.append(solution_coords[:, 0], solution_coords[0, 0])
    y = np.append(solution_coords[:, 1], solution_coords[0, 1])

    ax[0].plot(x, y, marker="o", linestyle="-")
    ax[0].set_title("Final Solution")
    ax[0].set_xlabel("X")
    ax[0].set_ylabel("Y")
    ax[0].set_aspect("equal")

    ax[1].plot(annealer.cost_history)
    ax[1].set_title("Distance History")
    ax[1].set_xlabel("Iteration")
    ax[1].set_ylabel("Distance")

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
        pass
    elif args.task == 2:
        if not args.input:
            print("Error: Input file required for task 2")
            return
        task2(args.input)
    else:
        print("Invalid task selected.")


if __name__ == "__main__":
    main()
