import json
import networkx as nx
import matplotlib.pyplot as plt

# Load in the core reactions json
core_rxn_json = json.load(open('core_rxn.json'))

# Load the ModelSeed compounds database
# If I don't want to add extra info to the nodes, I don't need this
met_json = json.load(open('../../ModelSEEDDatabase/Biochemistry/compounds.json'))

# Make a bipartite graph of the core reactions and compounds
G = nx.DiGraph()
for rxn in core_rxn_json:
    G.add_node(rxn['id'], bipartite='reaction') # By convention, should use 0 and 1 instead of 'reaction' and 'compound'
    if rxn['stoichiometry'] == '':
        continue
    for cpd_info in rxn['stoichiometry'].split(';'):
        cpd_id = cpd_info.split(':')[1]
        if cpd_id not in G.nodes():
            G.add_node(cpd_id, bipartite='compound') # TODO: Add info from the met_json
        if float(cpd_info.split(':')[0]) < 0:
            G.add_edge(cpd_id, rxn['id'], stoich=cpd_info.split(':')[0])
        else:
            G.add_edge(rxn['id'], cpd_id, stoich=cpd_info.split(':')[0])

# Save the graph
nx.write_graphml(G, 'core_network.graphml')

# Visualize the graph
nx.draw(G)
# Save the graph
plt.savefig('core_network.png')