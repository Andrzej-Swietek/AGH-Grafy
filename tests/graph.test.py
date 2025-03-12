import unittest
from unittest.mock import patch, MagicMock

from Lab01.main import process_graph, generate_random_graph

class TestMainFunctions(unittest.TestCase):

    @patch("lib.utils.graph_importer.GraphReader.read_adjacency_matrix", return_value=[[0, 1], [1, 0]])
    @patch("lib.utils.graph_importer.GraphWriter.write_adjacency_matrix")
    @patch("lib.utils.graph_importer.GraphWriter.write_adjacency_list")
    @patch("lib.utils.graph_importer.GraphWriter.write_incidence_matrix")
    @patch("lib.visualization.graph_visualizer.GraphVisualizer.draw")
    @patch("lib.visualization.graph_visualizer.GraphVisualizer.draw_natural")
    def test_process_graph(self, mock_draw, mock_draw_natural, mock_write1, mock_write2, mock_write3, mock_read):
        process_graph("../Lab01/data/adj_matrix.txt", "adjacency_matrix")
        mock_read.assert_called_once_with("fake_input.txt")
        mock_write1.assert_called()
        mock_write2.assert_called()
        mock_write3.assert_called()
        mock_draw.assert_called()
        mock_draw_natural.assert_called()

    @patch("lib.generators.RandomGraphGNK.generate")
    @patch("lib.utils.graph_importer.GraphWriter.write_adjacency_list")
    @patch("lib.visualization.graph_visualizer.GraphVisualizer.draw")
    def test_generate_random_graph_gnk(self, mock_draw, mock_write, mock_generate):
        mock_generate.return_value = MagicMock()
        generate_random_graph("gnk", 10, 15)
        mock_generate.assert_called()
        mock_write.assert_called()
        mock_draw.assert_called()

    @patch("lib.generators.RandomGraphGNP.generate")
    @patch("lib.utils.graph_importer.GraphWriter.write_adjacency_list")
    @patch("lib.visualization.graph_visualizer.GraphVisualizer.draw")
    def test_generate_random_graph_gnp(self, mock_draw, mock_write, mock_generate):
        mock_generate.return_value = MagicMock()
        generate_random_graph("gnp", 10, 0.3)
        mock_generate.assert_called()
        mock_write.assert_called()
        mock_draw.assert_called()

if __name__ == "__main__":
    unittest.main()