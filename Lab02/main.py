import argparse

from lib.core.converter import GraphConverter
from lib.generators.RandomGraphGNK import RandomGraphGNK
from lib.generators.RandomGraphGNP import RandomGraphGNP
from lib.utils.graph_importer import GraphWriter, GraphReader
from lib.visualization.graph_visualizer import GraphVisualizer
from lib.utils.sequence_checker import SequenceChecker
from lib.utils.components_finder import ComponentsFinder

GRAPHIC_SEQUENCE = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
NON_GRAPHIC_SEQUENCE = [4, 4, 3, 1, 2]


def task_one():
    print("Task 1")
    for seq in [GRAPHIC_SEQUENCE, NON_GRAPHIC_SEQUENCE]:
        print(f"Examined sequence: {seq}")
        graphic = SequenceChecker.is_graphic(seq)
        print(f"Is graphic: {graphic}")
        if graphic:
            graph = GraphConverter.from_graphic_sequence(seq)
            print("Visualizing graph...")
            GraphVisualizer.draw(graph)
            print("Visualization complete.")


def task_two():
    print("Task 2")
    n = 10
    print(f"Creating graph from graphic sequence: {GRAPHIC_SEQUENCE}")
    graph = GraphConverter.from_graphic_sequence(GRAPHIC_SEQUENCE)
    print("Graph created successfully.")
    print(f"Randomizing graph {n} times...")
    graph_randomized = GraphConverter.from_graphic_sequence(GRAPHIC_SEQUENCE)
    graph_randomized.randomize(n)
    print("Graph randomized successfully.")
    print("Comparing graphs...")
    GraphVisualizer.draw_side_by_side(graph, graph_randomized)
    print("Visualization complete.")


def task_three():
    print("Task 3")
    print(f"Creating graph from graphic sequence: {GRAPHIC_SEQUENCE}")
    graph = GraphConverter.from_graphic_sequence(GRAPHIC_SEQUENCE)
    print("Graph created successfully.")
    print("Randomizing graph until it is has more than 1 connected component...")
    graph_randomized = GraphConverter.from_graphic_sequence(GRAPHIC_SEQUENCE)
    n = 0
    while len(ComponentsFinder.find(graph_randomized)) == 1:
        graph_randomized.randomize(1)
        n += 1
    print(f"Graph randomized {n} times.")
    print("Graph components:")
    ComponentsFinder.print_components(ComponentsFinder.find(graph))
    print("Randomized graph components:")
    ComponentsFinder.print_components(ComponentsFinder.find(graph_randomized))
    print("Comparing graphs...")
    GraphVisualizer.draw_side_by_side(graph, graph_randomized)
    print("Visualization complete.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Grafy-Lab02")
    parser.add_argument(
        "-t", "--task", type=int, required=True, help="Select Task (1-6)"
    )
    args = parser.parse_args()

    if args.task == 1:
        task_one()

    elif args.task == 2:
        task_two()

    elif args.task == 3:
        task_three()
    else:
        print("Invalid task selected.")


if __name__ == "__main__":
    """
    1. Napisać program do sprawdzania, czy dana sekwencja liczb naturalnych
    jest ciągiem graficznym, i do konstruowania grafu prostego o stopniach
    wierzchołków zadanych przez ciąg graficzny.
    """
    """
    2. Napisać program do randomizacji grafów prostych o zadanych stopniach wierzchołków. Do tego celu wielokrotnie powtórzyć operację zamieniającą losowo wybraną parę krawędzi: ab i cd na parę ad i bc.
    """

    main()
