import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (países, capitales y vecinos)
data = [
    {"country": "USA", "capital": "Washington, D.C.", "population": 328.2, "currency": "USD", "neighbors": ["Canada", "Mexico"]},
    {"country": "Canada", "capital": "Ottawa", "population": 37.6, "currency": "CAD", "neighbors": ["USA"]},
    {"country": "Mexico", "capital": "Mexico City", "population": 126.2, "currency": "MXN", "neighbors": ["USA", "Guatemala"]},
    {"country": "Guatemala", "capital": "Guatemala City", "population": 17.2, "currency": "GTQ", "neighbors": ["Mexico", "Belize", "Honduras"]},
    {"country": "Belize", "capital": "Belmopan", "population": 0.4, "currency": "BZD", "neighbors": ["Guatemala", "Mexico"]},
    {"country": "Honduras", "capital": "Tegucigalpa", "population": 9.7, "currency": "HNL", "neighbors": ["Guatemala", "Nicaragua", "El Salvador"]},
    {"country": "Nicaragua", "capital": "Managua", "population": 6.5, "currency": "NIO", "neighbors": ["Honduras", "Costa Rica"]},
    {"country": "El Salvador", "capital": "San Salvador", "population": 6.4, "currency": "USD", "neighbors": ["Honduras"]},
    {"country": "Costa Rica", "capital": "San Jose", "population": 5.1, "currency": "CRC", "neighbors": ["Nicaragua", "Panama"]}
]
# Agregar nodos y relaciones
for item in data:
    G.add_node(item["country"], type="country", population=item["population"], currency=item["currency"])
    G.add_node(item["capital"], type="capital")
    G.add_edge(item["country"], item["capital"])

    for neighbor in item["neighbors"]:
        G.add_edge(item["country"], neighbor)

# Dibuja el grafo
pos = nx.spring_layout(G, seed=42)
node_labels = {node: node for node in G.nodes()}
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=800, node_color="skyblue", font_size=10, font_weight="bold")
edge_labels = {edge: f"{G.nodes[edge[0]]['currency']} {G.nodes[edge[0]]['population']}M" for edge in G.edges() if "type" in G.nodes[edge[1]] and G.nodes[edge[1]]["type"] == "country"}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

# Muestra el gráfico
plt.axis("off")
plt.show()