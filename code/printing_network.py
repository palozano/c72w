import networkx as nx
import numpy as np

# Parameters
N = 100

# Create graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([i from i in range(N)])

# Add edges
