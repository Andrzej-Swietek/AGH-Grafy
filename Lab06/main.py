import argparse

from Lab06.pagerank import DirectedGraph, PageRank


def main() -> None:
    parser = argparse.ArgumentParser(description='Grafy-Lab06')
    parser.add_argument('-t', '--task', type=int, required=True, help='Select Task (1, 2)')
    parser.add_argument('-i', '--input', type=str, help='Input file')
    args = parser.parse_args()

    match args.task:
        case 1:
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
                "L": ["A", "H"]
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

        case 2:
            pass
        case _:
            print("Invalid input: Select Task (1, 2)")


if __name__ == '__main__':
    main()