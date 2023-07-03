import networkx as nx
import matplotlib.pyplot as plt

# Read in the weighted graph
G = nx.read_graphml('core_network_weighted.graphml')

# Plot the distribution of weights
plt.hist([G.edges[edge]['weight'] for edge in G.edges()])

# Save the plot
plt.savefig('weight_distribution.png')