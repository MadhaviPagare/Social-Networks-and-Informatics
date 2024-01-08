#!/usr/bin/env python
# coding: utf-8




# The Girvan Newman’s Community detection algorithm is the basis for writing the following code in python.
#A hierarchical technique for identifying communities in complicated systems is called the Girvan–Newman algorithm 
#The concept is to use the edge betweenness centrality to determine which edges in a network occur most frequently between other pairs of nodes. 
#The edges connecting communities are then expected to have a high degree of edge betweenness.
#The network's underlying community structure will be much extremely fine once the edges with the highest betweenness are removed, 
#making communities much easier to catch.
#The data set that was retrieved from the karate.gml file is what we are using here to run the algorithm on.

#NetworkX is a Python package for creating, manipulating, and studying complex networks' structure, dynamics, and functions.
import networkx as nx

#https://www.analyticsvidhya.com/blog/2020/04/community-detection-graphs-networks/
#The Girvan-Newman approach, as we know, eliminates graph edges one by one based on the EBC score. 
#In order to remove the edge with the highest value,the first objective is to determine the EBC values for all of the edges. 
#The function below carries out the specified action:
def edge_to_remove(g):
    # edge_betweenness_centrality() function is used which is the total of the percentage of all-pairs shortest 
    #paths that cross through an edge e defines its betweenness centrality: 
    #where "sigma(s, t)" is the number of shortest (s, t)-pathways,
    #"sigma(s, t|e)" is the number of those paths passing through edge e, and "V" is the set of nodes
    dict_G = nx.edge_betweenness_centrality(g)
    edge = ()
    # The dictionary has been transformed into a list that can be used to discover the edge with the highest centrality value 
    #since we require that edge. A list of key value pairs is being sorted, and value is the parameter being considered. 
    #By default, the sorted() function returns a list; we should take it into a dict explicitly.
    #The sort method's second parameter, where the sorting criteria is defined, is a lambda function in this case. 
    #And since we're looking for the highest value, we set reverse to true to sort it in decreasing order.
    for key, value in sorted(dict_G.items(), key=lambda item: item[1], reverse = True):
      edge = key
      break
    return edge
# Main code
# First, using the dataset's karate.gml value, we use the function connected components to determine 
# whether it is a single graph or whether it comprises subgraphs ().
g = nx.read_gml('C:/Users/MADHAVI/Documents/SOCIAL NETWORKS/PROGRAMMING ASSIGNMENT 2/karate/karate/karate.gml',label = 'id')
#"A generator of sets of nodes, one for each component of G," is what nx.connected components(G) would produce. 
#Python's generators allow for lazy iteration over values which means it will generate the next item only when it is required.
a = nx.connected_components(g)
# The function connected components() produces a set, which we transform to a list to get its count.
lengthab = len(list(a))

while (lengthab == 1):
    # This loop will be used to eliminate each edge having the highest edge betweenness centrality, 
    #splitting the graph into two subgraphs.
    m, n = edge_to_remove(g)
    # With the use of the remove edge() method, we remove the edge that has the highest centrality value after obtaining it.
    g.remove_edge(m, n)
    # We again check the condition and loop through until the graph is divided into two communities.
    a = nx.connected_components(g)
    lengthab=len(list(a))

count = 1
#"A generator of sets of nodes, one for each component of G," is what nx.connected components(G) would produce. 
#Python's generators allow for lazy iteration over values which means it will generate the next item only when it is required.
a = nx.connected_components(g)
# We output the nodes in each community once the graph has been split into two sub graphs.
for i in a:
    print ("List on nodes in community ",count," are as follows")
    # As connected_components() gives collection of sets, we convert into lists and print it below.
    print (list(i))
    count = count +1






