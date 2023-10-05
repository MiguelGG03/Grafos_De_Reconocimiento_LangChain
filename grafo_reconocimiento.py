import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (países, capitales y vecinos)
data = [
    {"country": "USA", "capital": "Washington, D.C.", "neighbors": ["Canada", "Mexico"]},
    {"country": "Canada", "capital": "Ottawa", "neighbors": ["USA"]},
    {"country": "Mexico", "capital": "Mexico City", "neighbors": ["USA", "Guatemala"]},
    {"country": "Guatemala", "capital": "Guatemala City", "neighbors": ["Mexico", "Belize", "Honduras"]},
    {"country": "Belize", "capital": "Belmopan", "neighbors": ["Guatemala", "Mexico"]},
    {"country": "Honduras", "capital": "Tegucigalpa", "neighbors": ["Guatemala", "Nicaragua", "El Salvador"]},
    {"country": "Nicaragua", "capital": "Managua", "neighbors": ["Honduras", "Costa Rica"]},
    {"country": "El Salvador", "capital": "San Salvador", "neighbors": ["Honduras"]},
    {"country": "Costa Rica", "capital": "San Jose", "neighbors": ["Nicaragua", "Panama"]}
]

# Agregar nodos y relaciones
for item in data:
    G.add_node(item["country"], type="country")
    G.add_node(item["capital"], type="capital")
    G.add_edge(item["country"], item["capital"])

    for neighbor in item["neighbors"]:
        G.add_edge(item["country"], neighbor)

# Dibuja el grafo
pos = nx.spring_layout(G, seed=42)
node_labels = {node: node for node in G.nodes()}
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=800, node_color="skyblue", font_size=10, font_weight="bold")
edge_labels = {(country, neighbor): neighbor for country, neighbor in G.edges() if G.nodes[neighbor]["type"] == "country"}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

# Muestra el gráfico
plt.axis("off")
plt.show()
