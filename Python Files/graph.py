import networkx as nx
import matplotlib.pyplot as plt

# Create a NetworkX graph
G = nx.Graph()

# Add nodes (politicians)
# For demonstration purposes, replace node IDs and labels with your actual data
G.add_node(1, label="Politician 1")
G.add_node(2, label="Politician 2")
# Add more nodes as needed

# Add edges (voting proximity relationships)
# For demonstration purposes, replace edge tuples with your actual data
G.add_edge(1, 2, weight=0.8)
# Add more edges as needed

# Apply Fruchterman-Reingold layout
pos = nx.spring_layout(G)

# Draw the network
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10)

# Show the plot
plt.show()
