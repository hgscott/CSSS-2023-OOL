import networkx as nx
import pandas as pd

# Read in the weighted graph
G = nx.read_graphml('core_network_weighted.graphml')

# Make a pandas dataframe with the metabolites as rows and the reactions as columns
# The values in the dataframe are the edge weight (the number of times the reaction is in a GEM)
G_matrix = pd.DataFrame(index=[node for node in G.nodes() if G.nodes[node]['bipartite'] == 'compound'],
                        columns=[node for node in G.nodes() if G.nodes[node]['bipartite'] == 'reaction'])
# Fill in the dataframe with all 0s
# Because the edges that do not exist (i.e. are not possible reactions) do not hae any weight
G_matrix = G_matrix.fillna(0)
# Fill in the dataframe with the edge weights for the actual reactions
for edge in G.edges():
    if G.nodes[edge[0]]['bipartite'] == 'compound':
        G_matrix.loc[edge[0], edge[1]] = G.edges[edge]['weight']
    else:
        G_matrix.loc[edge[1], edge[0]] = G.edges[edge]['weight']

# Save as a csv
G_matrix.to_csv('core_network_weighted.csv')