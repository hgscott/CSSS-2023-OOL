import json
import os
import networkx as nx

# Assign directory where the GEMs are stored
directory = 'GEMs'

# Load in the universal graph
G = nx.read_graphml('core_network.graphml')

# Give edge a weight of 0
for edge in G.edges():
    G.edges[edge]['weight'] = 0
 
# Loop through all the GEMs
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(f):
        continue
    if not filename.endswith('.json'):
        continue
    # Load in the GEM
    with open(f) as f:
        gem = json.load(f)
        # For each GEM, loop through all the reactions
        for rxn in gem['modelreactions']:
            # Split the compartment name off of the reaction id
            rxn_id = rxn['id'].split('_')[0]
            # Skip if the reaction ID is not in the core network
            if rxn_id not in G.nodes():
                # TODO: Throw a warning
                continue
            # Increase the weight of all the edges to/from that reaction by 1
            # Assuming that a reaction alwys has the same stoichiometry
            for edge in G.edges(rxn_id):
                G.edges[edge]['weight'] += 1

# Save the graph
nx.write_graphml(G, 'core_network_weighted.graphml')