# TODOs

# - Use JSON data coming from API Request
# - add node with only selected attributes
# - idenitfy what is regarded as the label for node on addition of node to plot correct network graph
# - Break into Class and method for efficiency

import networkx as nx
import json
import os
import matplotlib.pyplot as plt

from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

class GraphStats:
    def __init__(self, nodes, edges, directed, linkAttribute):
        self.nodes = nodes
        self.edges = edges
        self.directed = directed
        self.linkAttribute = linkAttribute
        self.G = ''
    
    def getGraphStats(self):
        # Initialize Graph
        if self.directed:
            self.G = nx.DiGraph()
        else:
            self.G = nx.Graph()

        attrs = {}

        # Add check to avoid error when no nodes and edges

        # Add Nodes
        for i in range(len(self.nodes) - 1):
            attribute = self.linkAttribute
            node_value = self.nodes[i][attribute]
            self.G.add_node(node_value)
            attrs[node_value] = {}
            # Can be specific to what attributes to only include rather than adding all
            for attr in self.nodes[0].keys():
                if attr != self.linkAttribute:
                    attrs[node_value].update({
                        attr: self.nodes[i][attr]
                    })

        # Add Selected Attributes
        nx.set_node_attributes(self.G, attrs)

        # Add Edges
        for i in range(len(self.edges) - 1):
            print(len(self.edges))
            print(i)
            source =  self.edges[i]["source"]
            print(i)
            target = self.edges[i]["target"]
            self.G.add_edge(source, target)

        graph_stats_json = {
            "total_edges": nx.number_of_edges(self.G),
            "total_nodes": nx.number_of_nodes(self.G),
            "density": nx.density(self.G),
            "average_clustering_coefficient": nx.average_clustering(self.G),
            # Only Directed Graphs have strongly connected components
            "number_of_strongly_connected_components": nx.number_strongly_connected_components(self.G)
                if nx.is_directed(self.G) else 0,
            "reciprocity": nx.reciprocity(self.G),
            # Adjust into proper format since this is converted into a list for JSON return only
            "adj_matrix": nx.adjacency_matrix(self.G).todense().tolist()
        }
        return graph_stats_json
        
        # print(nx.to_edgelist(G))``

graph_stats_page = Blueprint('graph_stats', __name__)
@graph_stats_page.route('/graph-stats', methods=['POST'])
@cross_origin()
def graph_stats_return():
    data = request.get_json(force=True)
    nodes = data["nodes"] or []
    edges = data["edges"] or []
    directed = data["directed"] or False
    linkAttribute = data["linkAttribute"] or ""
    graph_stats = GraphStats(nodes, edges, directed, linkAttribute)
    graph_stats.getGraphStats()
    return graph_stats.getGraphStats(), 200

    # Take graph as json ani use that to takeout the statisticss