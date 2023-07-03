import json
import pandas as pd

# Load the ModelSeed compounds database
met_json = json.load(open('../../ModelSEEDDatabase/Biochemistry/compounds.json'))

# Load the ModelSeed reactions database
rxn_json = json.load(open('../../ModelSEEDDatabase/Biochemistry/reactions.json'))

# Load the ModelSeed Core database
core_rxns = pd.read_csv('../../ModelSEEDDatabase/Templates/Core/Reactions.tsv', sep='\t')

# Subset the reactions json to only include the core reactions
core_rxn_json = [rxn for rxn in rxn_json if rxn['id'] in core_rxns['id'].tolist()]

# Save the core reactions json
with open('core_rxn.json', 'w') as f:
    json.dump(core_rxn_json, f)