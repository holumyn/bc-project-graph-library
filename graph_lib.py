class Graph_lib(object):
	"""
	Graph Library that handles traversals,
	both Depth First Search and Breath First Search 
	"""
	def __init__(self):
		pass
	
	def dfs(self,graph,start):
		visited = []
		stack = [start]

		while stack:
			node = stack.pop()

			if node not in visited:
				visited.append(node)
				stack.extend([x for x in graph[node] if x not in visited])

		return visited
	
	def bfs(self):
		pass

		

	

	