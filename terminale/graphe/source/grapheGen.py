import matplotlib.pyplot as plt
import networkx as nx

# Helper function to draw a graph with required style
def draw_graph(G):
    plt.figure(figsize=(6, 6))
    plt.margins(0.3)
    pos = nx.spring_layout(G, seed=42)  # consistent layout
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="white",     # sommet non bleu
        edgecolors="black",
        node_size=4000,      # larger nodes
        width=1,           # thinner edges
        font_size=14
    )
    plt.show()

# Graph 1
G1 = nx.Graph()
G1.add_edges_from([("A", "B"), ("A", "C"), ("A", "D"), ("C", "D"), ("B", "D"),("C","B")])
draw_graph(G1)
