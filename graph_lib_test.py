"""Unit test for Class Graph_lib"""
import unittest
from graph_lib import Graph_lib

class GraphLibTestSuite(unittest.TestCase):
	def test_dfs_wt_value(self):
		"""
		Test the depth first search with a graph
		"""
		graph = {0:[1,5],1:[0,2,3],2:[1,4],3:[1,4,5],4:[2,3,5],5:[0,3,4]}
		res = Graph_lib.dfs(self,graph,0)
		self.assertEqual(res, [0, 5, 4, 3, 1, 2])

	

if __name__ == '__main__':
	unittest.main()