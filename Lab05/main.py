import argparse

from lib.generators.GenerateFlowNetwork import RandomFlowNetwork
from lib.visualization.graph_visualizer import GraphVisualizer
from lib.finders.max_flow_finder import MaxFlowFinder

def generate_random_flow_network(N: int, param: float):
    generator = RandomFlowNetwork(N, param)
    graph = generator.generate()
    print("Generating visualizations...")
    GraphVisualizer.draw_flow_network(graph)
    print("Visualization complete.")
    return graph

def task_one(N: int):
    generate_random_flow_network(N, 0.5)
    

def task_two(N: int):
    network = generate_random_flow_network(N, 0.5)
    MaxFlowFinder.find(network)


def main():
    parser = argparse.ArgumentParser(description="Grafy-Lab05")
    parser.add_argument("-t", "--task", type=int, required=True, help="Select Task (1-4)")
    parser.add_argument('-n', '--layers', type=int, help='Number of layers')
    args = parser.parse_args()
    
    tasks = [task_one, task_two]
    if args.task == 1:
        if not args.layers:
            print("Error: Number of layers required for task 1")
            return
        task_one(args.layers)
    elif args.task == 2:
        if not args.layers:
            print("Error: Number of layers required for task 2")
            return
        task_two(args.layers)
    else:
        print("Invalid task selected.")

if __name__ == "__main__":
    """
    1. Napisać program do tworzenia losowej sieci przepływowej między pojedynczym źródłem i pojedynczym ujściem według następującej procedury.
    Na potrzeby programu wprowadzić warstwy, które idą od źródła do ujścia. Źródło znajduje się w zerowej warstwie a ujście w warstwie
    N + 1. Liczba pośrednich warstw wynosi N i jest parametrem programu (N ≥ 2, a na potrzeby testowania N ≤ 4). Pośrednie warstwy
    ponumerowane są od 1 do N. W każdej pośredniej warstwie rozmieścić losowo od dwóch do N wierzchołków. Połączyć wierzchołki kolejnych
    warstw za pomocą łuków skierowanych od warstwy i do warstwy i + 1 (∀i = 0, . . . , N), tak aby z każdego wierzchołka leżącego w warstwie i
    wychodził co najmniej jeden łuk i do każdego wierzchołka w warstwie i + 1 wchodził co najmniej jeden łuk. Do otrzymanego w ten sposób digrafu 
    należy następnie dodać 2N łuków w sposób losowy. Łuki mają być losowane bez preferencji kierunku, tzn. nie muszą być skierowane zgodnie z warstwami. 
    Należy jednak zwrócić uwagę, żeby nie dodać łuku już istniejącego i żeby nie dodać łuku wchodzącego do źródła albo wychodzącego z ujścia. 
    Na tak otrzymanym digrafie przypisać każdemu łukowi liczbę naturalną z zakresu [1, 10] mającą interpretację przepustowości. Zakodować i narysować otrzymaną sieć.
    """

    """
    2.  Zastosować algorytm Forda-Fulkersona do znalezienia maksymalnego przepływu na sieci z zadania pierwszego. 
    Ścieżki powiększające wybierać jako ścieżki o najmniejszej liczbie krawędzi. Do ich wyszukiwania użyć przeszukiwania wszerz.
    """

    main()