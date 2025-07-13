import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Read Proximity and Party Affiliation Data from Text File
proximity_file = 'investmentproximity.txt'  # Replace with the path to your proximity data file
party_file = 'partyaffiliation.txt'   # Replace with the path to your party affiliation data file

with open(proximity_file, 'r') as f:
    proximity_lines = f.readlines()

with open(party_file, 'r') as f:
    party_lines = f.readlines()

# Step 2: Create Proximity Matrix and Add Party Affiliation as Node Attributes
proximity_matrix = []
party_affiliation = {}

for i, line in enumerate(proximity_lines):
    row = [float(val) for val in line.split()]
    proximity_matrix.append(row)
    
    # Assuming party affiliation data corresponds to the rows of the proximity matrix
    # Adjust indexing as needed
    if i < len(party_lines):
        party = int(party_lines[i])  # Assuming party is represented as 1 for Republican and 0 for Democrat
        party_affiliation[i] = 'Republican' if party == 1 else 'Democrat'

# Step 3: Convert Proximity Matrix to Graph and Add Node Attributes
G = nx.from_numpy_array(np.array(proximity_matrix))

# Add party affiliation as node attributes
nx.set_node_attributes(G, party_affiliation, 'party')

# Step 4: Apply Fruchterman-Reingold Layout
pos = nx.spring_layout(G)

# Step 5: Visualize the Network with Color-Coded Nodes for Party Affiliation
plt.figure(figsize=(8, 6))

# Separate nodes by party affiliation for coloring
republican_nodes = [node for node, data in G.nodes(data=True) if data['party'] == 'Republican']
democrat_nodes = [node for node, data in G.nodes(data=True) if data['party'] == 'Democrat']

# Draw Republican nodes
nx.draw_networkx_nodes(G, pos, nodelist=republican_nodes, node_color='red', node_size=3000, alpha=0.8)

# Draw Democrat nodes
nx.draw_networkx_nodes(G, pos, nodelist=democrat_nodes, node_color='blue', node_size=3000, alpha=0.8)

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10)

plt.title('Voting Proximity Network with Party Affiliation')
plt.axis('off')
plt.show()