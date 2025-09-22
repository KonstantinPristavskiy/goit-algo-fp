import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

from collections import deque

def generate_colors(n):
    """Генерація n кольорів від темного до світлого."""
    colors = []
    for i in range(n):
        # Інтерполяція від темного синього до світло-блакитного
        red = int(0 + (173 - 0) * (i / (n - 1))) if n > 1 else 0
        green = int(0 + (216 - 0) * (i / (n - 1))) if n > 1 else 216
        blue = int(139 + (230 - 139) * (i / (n - 1))) if n > 1 else 230
        colors.append(f'#{red:02x}{green:02x}{blue:02x}')
    return colors

def dfs_traversal(root):
    if not root:
        return []
    
    visited_order = []
    stack = [root]

    while stack:
        node = stack.pop()
        visited_order.append(node)
        
        # Додаємо нащадків у стек (спочатку правий, потім лівий, щоб обхід був pre-order)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return visited_order

def bfs_traversal(root):
    if not root:
        return []
        
    visited_order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited_order.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return visited_order

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в глибину (DFS)
dfs_nodes = dfs_traversal(root)
dfs_colors = generate_colors(len(dfs_nodes))
for node, color in zip(dfs_nodes, dfs_colors):
    node.color = color

draw_tree(root, "DFS Traversal")


# Скидання кольорів до початкових
for node in dfs_nodes:
    node.color = "skyblue"

# Обхід в ширину (BFS)
bfs_nodes = bfs_traversal(root)
bfs_colors = generate_colors(len(bfs_nodes))
for node, color in zip(bfs_nodes, bfs_colors):
    node.color = color

draw_tree(root, "BFS Traversal")
