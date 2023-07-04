library(bipartite)

# Read in the CSV file of the graph
# Throws an error, but seems to work
weighted_reactions <- read.csv("core_network_weighted.csv")

# Set the row names to the be metabolite IDs and remove that column
# Throws an error, but seems to work
rownames(weighted_reactions) <- weighted_reactions[, 1]
weighted_reactions <- weighted_reactions[, -1]

# Compute modules
mod <- computeModules(web=weighted_reactions)

# Plot the resulting modules
plotModuleWeb(mod)