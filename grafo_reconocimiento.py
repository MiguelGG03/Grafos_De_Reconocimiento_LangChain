import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (países y capitales)
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington, D.C.", "Ottawa", "Mexico City"]

for country, capital in zip(countries, capitals):
    G.add_edge(country, capital)

# Dibuja el grafo
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=10, font_weight="bold")

# Muestra el gráfico
plt.axis("off")
plt.show()
