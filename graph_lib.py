"""
  Graph Library that handles traversals,
  both Depth First Search and Breath First Search 

"""
import click
from collections import deque


@click.command()
@click.option('--option1', prompt='Instruction: Enter 1 for Graph 1 or 2 for Graph 2 or 3 for Graph 3(BFS)\n',
              help='User input')
@click.option('--search', prompt='Enter DFS for Depth First Search or BFS for Breadth First Search:\n',
              help='User search')
def opt(option1, search):
	if option1 == '1' and search == 'DFS':
		g1 = {0:[1,5],1:[0,2,3],2:[1,4],3:[1,4,5],4:[2,3,5],5:[0,3,4]}
		click.echo('\nResult: ')
		dfs(g1,0)

	elif option1 == '2' and search == 'DFS':

		g2 = {'A':['B','C'],'B':['A','D','E'],'C':['A','F'],'D':['B'],'E':['B','F'],'F':['C','E']}
		click.echo('\nResult: ')
		dfs(g2,'A')

	elif option1 == '3' and search == 'BFS':

		g2 = {'A':['B','C'],'B':['A','D','E'],'C':['A','F'],'D':['B'],'E':['B','F'],'F':['C','E']}
		g3={'A':{'F','G'},'B':{'S','F'},'C':{'D','E','Z'},'D':{'C','S'},'E':{'F','C'},'F':{'E','B','A'},'G':{'A'}, 'S':{'B','D'},'Z':{'C'}}
		click.echo('\nResult: ')
		click.echo(bfs(g2,'A','Z'))

	else:
		click.echo('\nYou entered an invalid option. Try again')


		
def dfs(graph,start):
    """
    performs depth first search(dfs) on a graph

    Args: visited: visited nodes list
        stack: stores the next node value

    Return: List of a list of visited nodes
    """
		visited = []
		stack = [start,]

		while stack:
			node = stack.pop()

			if node not in visited:
				visited.append(node)
				stack.extend([x for x in graph[node] if x not in visited])

		click.echo(visited)

def bfs(graph, start, end):
    """
    performs Breadth first search(bfs) on a graph

    Args: graph: A specified graph
          start: The starting node of the graph
          end: the end node of the graph

    Return: A list of the path from start to end
    """
    
    queue = []
    queue.append([start])
    while queue:
      path = queue.pop(0)
      node = path[-1]
      
      if node == end:
        return path
       
      for adjacent in graph.get(node, []):
        new_path = list(path)
        new_path.append(adjacent)
        queue.append(new_path)
    click.echo(queue)





if __name__ == '__main__':
	click.echo("Welcome user! \n")
	click.echo("Graph 1: {0:[1,5],1:[0,2,3],2:[1,4],3:[1,4,5],4:[2,3,5],5:[0,3,4]}")
	click.echo("Graph 2: {'A':['B','C'],'B':['A','D','E'],'C':['A','F'],'D':['B'],'E':['B','F'],'F':['C','E']}\n")


	opt()
