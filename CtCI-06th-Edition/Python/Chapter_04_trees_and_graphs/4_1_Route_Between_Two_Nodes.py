'''
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
'''
from collections import deque
import pytest
class Node:
    def __init__(self, data):
        self.data
        self.nodes = [Node]
        self.marked = False

def Route_Between_Nodes_BFS(node, data):
    q = deque()
    print(node.data)
    node.marked = True

    q.append(node) #Add to the end of the queue 
    while len(q) > 0:
        node = Node(q.popleft())
        if node.data == data:
            print(node.data)
            return 
        
        for n in node.nodes:
            if n.marked == True:
                q.append(n)

def route_between_nodes_bfsII(graph, root, data):
    if root == data:
        return True
    
    queue = deque()
    visited = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            if adjacent not in visited:
                if adjacent == data:
                    return True
                else:
                    queue.append(adjacent)
        visited.append(node)
    return False

'''
q = deque()
q.append('a')
q.append('b')
q.append('c')
print(f"Initial queue \n{q}")
print("Starting to dequeue")
while len(q) > 0:
    print(q.popleft())
print(f"queue after removing elements {q}")
'''

graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

def bfs(graph, start, data):
    if start == data:
        return True
    
    queue = deque()
    visited = []

    queue.append(start)

    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            if adjacent not in visited:
                if adjacent == data:
                    return True
                else:
                    queue.append(adjacent)
        visited.append(node)
    
    return False

@pytest.mark.parametrize(
    'graph, root, data, expected',
    [
        (graph, 'A', 'L', True),
        (graph, 'A', 'B', True)
    ]
)
def test_route_between_nodes_bfsII(graph, root, data, expected):
    assert route_between_nodes_bfsII(graph,root,data) == expected
    
@pytest.mark.parametrize(
    'graph, root, data, expected',
    [
        (graph, 'A', 'L', True),
        (graph, 'A', 'B', True)
    ]
)
def test_bfs(graph, root, data, expected):
    assert bfs(graph,root,data) == expected