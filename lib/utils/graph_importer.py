class GraphReader:
    @staticmethod
    def read_adjacency_matrix(filename: str) -> List[List[int]]:
        """
        Czyta macierz sąsiedztwa z pliku.
        Format pliku: każda linia to wiersz macierzy, wartości oddzielone spacjami.
        """
        with open(filename, 'r') as file:
            matrix = []
            for line in file:
                row = list(map(int, line.strip().split()))
                matrix.append(row)
            return matrix

    @staticmethod
    def read_adjacency_list(filename: str) -> Dict[int, List[int]]:
        """
        Czyta listę sąsiedztwa z pliku.
        Format pliku: każda linia to "wierzchołek: sąsiad1 sąsiad2 ..."
        """
        with open(filename, 'r') as file:
            adjacency_list = {}
            for line in file:
                parts = line.strip().split(':')
                vertex = int(parts[0])
                neighbors = list(map(int, parts[1].strip().split()))
                adjacency_list[vertex] = neighbors
            return adjacency_list

    @staticmethod
    def read_incidence_matrix(filename: str) -> List[List[int]]:
        """
        Czyta macierz incydencji z pliku.
        Format pliku: każda linia to wiersz macierzy, wartości oddzielone spacjami.
        """
        with open(filename, 'r') as file:
            matrix = []
            for line in file:
                row = list(map(int, line.strip().split()))
                matrix.append(row)
            return matrix

class GraphWriter:
    @staticmethod
    def write_adjacency_matrix(graph: Graph, filename: str):
        """
        Zapisuje macierz sąsiedztwa do pliku.
        """
        matrix = graph.to_adjacency_matrix()
        with open(filename, 'w') as file:
            for row in matrix:
                file.write(' '.join(map(str, row)) + '\n')

    @staticmethod
    def write_adjacency_list(graph: Graph, filename: str):
        """
        Zapisuje listę sąsiedztwa do pliku.
        """
        adjacency_list = graph.to_adjacency_list()
        with open(filename, 'w') as file:
            for vertex, neighbors in adjacency_list.items():
                file.write(f"{vertex}: {' '.join(map(str, neighbors))}\n")

    @staticmethod
    def write_incidence_matrix(graph: Graph, filename: str):
        """
        Zapisuje macierz incydencji do pliku.
        """
        incidence_matrix = graph.to_incidence_matrix()
        with open(filename, 'w') as file:
            for row in incidence_matrix:
                file.write(' '.join(map(str, row)) + '\n')