import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (países y capitales)
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington, D.C.", "Ottawa", "Mexico City"]

for country, capital in zip(countries, capitals):
    G.add_edge(country, capital)
