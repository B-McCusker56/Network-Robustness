import networkx as nx
import numpy as np
import random
import math
from operator import itemgetter

def commonNeighbors(G, num_iter):
	H = G.__class__()
	H.add_nodes_from(G)
	H.add_edges_from(G.edges)
	for i in range(num_iter):
		print(H.number_of_edges())
		linkPredictions = []
		for v in H.nodes():
			for u in H.nodes():
				if v > u and H.has_edge(v, u) == False:
					numCommonNeighbors = len(set(H.neighbors(v)).intersection(set(H.neighbors(u))))
					if numCommonNeighbors > 0:
						linkPredictions.append((int(numCommonNeighbors), u, v))
		bestLink = max(linkPredictions, key = itemgetter(0))
		print(bestLink)
		H.add_edge(bestLink[1], bestLink[2])



G = nx.read_gml("power.gml", label='id')
# print(G.nodes)
# print(G.edges)
# print(G)
commonNeighbors(G, 5)
print(G)


