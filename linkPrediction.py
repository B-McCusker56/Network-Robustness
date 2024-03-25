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
		#change this to G after testing
		H.add_edge(bestLink[1], bestLink[2])

def preferentialAttachment(G, num_iter):
	H = G.__class__()
	H.add_nodes_from(G)
	H.add_edges_from(G.edges)
	for i in range(num_iter):
		print(H.number_of_edges())
		linkPredictions = []
		for v in H.nodes():
			for u in H.nodes():
				if v > u and H.has_edge(v, u) == False:
					attachmentValue = len(set(H.neighbors(v))) * len(set(H.neighbors(u)))
					if attachmentValue > 0:
						linkPredictions.append((int(attachmentValue), u, v))
		bestLink = max(linkPredictions, key = itemgetter(0))
		print(bestLink)
		#change this to G after testing
		H.add_edge(bestLink[1], bestLink[2])

def jaccardIndex(G, num_iter):
	H = G.__class__()
	H.add_nodes_from(G)
	H.add_edges_from(G.edges)
	for i in range(num_iter):
		print(H.number_of_edges())
		linkPredictions = []
		degreeMax = sorted([d for n, d in G1.degree()], reverse=True)[0]
		for v in H.nodes():
			for u in H.nodes():
				if v > u and H.has_edge(v, u) == False:
					jaccardIndex = (len(set(H.neighbors(v)).intersection(set(H.neighbors(u)))) \
						/ len(set(H.neighbors(v)).union(set(H.neighbors(u))))) \
						* degreeMax
					if jaccardIndex > 0:
						linkPredictions.append((int(jaccardIndex), u, v))
		bestLink = max(linkPredictions, key = itemgetter(0))
		print(bestLink)
		#change this to G after testing	
		H.add_edge(bestLink[1], bestLink[2])

def adamicAdarIndex(G, num_iter):
	H = G.__class__()
	H.add_nodes_from(G)
	H.add_edges_from(G.edges)
	for i in range(num_iter):
		print(H.number_of_edges())
		linkPredictions = []
		for v in H.nodes():
			for u in H.nodes():
				if v > u and H.has_edge(v, u) == False:
					Nv_intersect_Nu = set(H.neighbors(v)).intersection(set(H.neighbors(u)))
					for x in Nv_intersect_Nu:
						adamicAdarIndex += 1 / (math.log10(len(set(H.neighbors(x)))))
					if adamicAdarIndex > 0:
						linkPredictions.append((int(adamicAdarIndex), u, v))
		bestLink = max(linkPredictions, key = itemgetter(0))
		print(bestLink)
		#change this to G after testing
		H.add_edge(bestLink[1], bestLink[2])

def katzMeasure(G, beta, num_iter):
	H = G.__class__()
	H.add_nodes_from(G)
	H.add_edges_from(G.edges)
	for i in range(num_iter):
		print(H.number_of_edges())
		linkPredictions = []
		for v in H.nodes():
			for u in H.nodes():
				if v > u and H.has_edge(v, u) == False:
					vuPaths = list(nx.shortest_simple_paths(G,v,u))
					numPathsOfLenL = []
					for path in vuPaths:
						numPathsOfLenL[len(path)] += 1;
					katzCentrality = 0
					currentLength = 0
					#for numKPaths in numPathsOfLenL:
					#	try:
					#		katzCentrality += beat**currentLength * numKPaths[currentLength]
					if katzCentrality > 0:
						linkPredictions.append((int(katzCentrality), u, v))
		bestLink = max(linkPredictions, key = itemgetter(0))
		print(bestLink)
		#change this to G after testing
		H.add_edge(bestLink[1], bestLink[2])	



G = nx.read_gml("power.gml", label='id')
# print(G.nodes)
# print(G.edges)
# print(G)
katzMeasure(G,0.0002, 5)
print(G)


