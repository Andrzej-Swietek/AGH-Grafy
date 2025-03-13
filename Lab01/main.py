import argparse

from lib.core.converter import GraphConverter
from lib.generators.RandomGraphGNK import RandomGraphGNK
from lib.generators.RandomGraphGNP import RandomGraphGNP
from lib.utils.graph_importer import GraphWriter, GraphReader
from lib.visualization.graph_visualizer import GraphVisualizer


def process_graph(input_file: str, input_type: str):
    if input_type == "adjacency_matrix":
        matrix = GraphReader.read_adjacency_matrix(input_file)
        graph = GraphConverter.from_adjacency_matrix(matrix)
    elif input_type == "adjacency_list":
        adjacency_list = GraphReader.read_adjacency_list(input_file)
        graph = GraphConverter.from_adjacency_list(adjacency_list)
    elif input_type == "incidence_matrix":
        incidence_matrix = GraphReader.read_incidence_matrix(input_file)
        graph = GraphConverter.from_incidence_matrix(incidence_matrix)
    else:
        raise ValueError("Invalid input type")

    print("Graph loaded successfully. Converting representations...")
    GraphWriter.write_adjacency_matrix(graph, "output_adjacency_matrix.txt")
    GraphWriter.write_adjacency_list(graph, "output_adjacency_list.txt")
    GraphWriter.write_incidence_matrix(graph, "output_incidence_matrix.txt")

    print("Graph representations saved. Generating visualizations...")
    GraphVisualizer.draw(graph)
    GraphVisualizer.draw_natural(graph)
    print("Visualization complete.")

    print("Graph loaded successfully. Converting representations...")
    GraphWriter.write_adjacency_matrix(graph, "output_adjacency_matrix.txt")
    GraphWriter.write_adjacency_list(graph, "output_adjacency_list.txt")
    GraphWriter.write_incidence_matrix(graph, "output_incidence_matrix.txt")

    print("Graph representations saved. Generating visualizations...")
    GraphVisualizer.draw(graph)
    GraphVisualizer.draw_natural(graph)
    print("Visualization complete.")


def generate_random_graph(mode: str, n: int, param: float):
    if mode == "gnk":
        generator = RandomGraphGNK(n, int(param))
    elif mode == "gnp":
        generator = RandomGraphGNP(n, param)
    else:
        raise ValueError("Invalid generation mode")

    graph = generator.generate()
    print("Random graph generated successfully.")
    GraphWriter.write_adjacency_list(graph, "random_graph.txt")
    GraphVisualizer.draw(graph)


def main() -> None:
    parser = argparse.ArgumentParser(description='Grafy-Lab01')
    parser.add_argument('-t', '--task', type=int, required=True, help='Select Task (1, 2, 3)')
    parser.add_argument('-i', '--input', type=str, help='Input file')
    parser.add_argument('-m', '--mode', type=str, help='Graph generation mode (gnk/gnp)')
    parser.add_argument('-n', '--vertices', type=int, help='Number of vertices')
    parser.add_argument('-p', '--param', type=float, help='Edge count (gnk) or probability (gnp)')
    args = parser.parse_args()

    if args.task == 1:
        if not args.input:
            print("Error: Input file required for task 1")
            return

        if "adj_list" in args.input:
            process_graph(args.input, "adjacency_list")
        elif "adj_matrix" in args.input:
            process_graph(args.input, "adjacency_matrix")
        elif "incidence_matrix" in args.input:
            process_graph(args.input, "incidence_matrix")
        else:
            print("Error: Unknown file format. Expected 'adj_list', 'adj_matrix', or 'incidence_matrix' in filename.")

    elif args.task == 2:
        if not args.input:
            print("Error: Input file required for task 2")
            return
        process_graph(args.input, "adjacency_matrix")
    elif args.task == 3:
        if not args.mode or not args.vertices or args.param is None:
            print("Error: Mode, number of vertices, and parameter required for task 3")
            return
        generate_random_graph(args.mode, args.vertices, args.param)
    else:
        print("Invalid task selected.")


if __name__ == '__main__':
    """
      1. Napisać program kodujący grafy proste za pomocą macierzy sąsiedztwa, macierzy incydencji i list sąsiędztwa. 
      Stworzyć moduł do zmianydanego kodowania na pozostałe.
    """

    """
      2.  Napisać program do wizualizacji grafów prostych używający reprezentacji, w której wierzchołki grafu są równomiernie rozłożone na okręgu.
    """

    """
      3. Napisać program do generowania grafów losowych G(n, l) oraz G(n, p).
    """

    main()
