import json
import os
import networkx as nx

# Assign directory where the GEMs are stored
directory = 'GEMs'

# Load in the universal graph
G = nx.read_graphml('core_network.graphml')
 
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
            for cpd_info in rxn['stoichiometry'].split(';'):
                cpd_id = cpd_info.split(':')[1]
                if cpd_id not in G.nodes():
                    G.add_node(cpd_id, bipartite='compound') # TODO: Add info from the met_json
                if float(cpd_info.split(':')[0]) < 0:
                    G.add_edge(cpd_id, rxn['id'], stoich=cpd_info.split(':')[0])
                else:
                    G.add_edge(rxn['id'], cpd_id, stoich=cpd_info.split(':')[0])