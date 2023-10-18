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

        # For Degree Distribution
        degree_sequence = sorted((degree for n, degree in self.G.degree()))
        unique_degree_list = list(dict.fromkeys(degree_sequence))
        unique_degree_count = []

        for degree in unique_degree_list:
            unique_degree_count.append(degree_sequence.count(degree))

        if (self.directed):
            # For In Degree Distribution
            in_degree_sequence = sorted((degree for n, degree in self.G.in_degree()))
            unique_in_degree_list = list(dict.fromkeys(in_degree_sequence))
            unique_in_degree_count = []

            for in_degree in unique_in_degree_list:
                unique_in_degree_count.append(in_degree_sequence.count(in_degree))

            # For Out Degree Distribution
            out_degree_sequence = sorted((degree for n, degree in self.G.out_degree()))
            unique_out_degree_list = list(dict.fromkeys(out_degree_sequence))
            unique_out_degree_count = []

            for out_degree in unique_out_degree_list:
                unique_out_degree_count.append(out_degree_sequence.count(out_degree))

        graph_stats_json = {
            "graph_summary": {
                "total_edges": nx.number_of_edges(self.G),
                "total_nodes": nx.number_of_nodes(self.G),
                # "max_degree": 0,
                # "min_degree": 0,
                # "average_degree": 0,
                # "median_degree": 0,
                "reciprocity": nx.reciprocity(self.G) if nx.is_directed else 0,
            },
            "graph_connectivity": {
                "strongly_connected_components": nx.number_strongly_connected_components(self.G)
                                if nx.is_directed(self.G) else 0,
                "weakly_connected_components": nx.number_weakly_connected_components(self.G)
                                if nx.is_directed(self.G) else 0,
                "largest_strongly_connected_component_size": len(max(nx.strongly_connected_components(self.G), key=len)) if nx.is_directed(self.G) else 0
            },
            "graph_clustering": {
                "transitivity": nx.transitivity(self.G),
                "average_clustering_coefficient": nx.average_clustering(self.G),
                "density": nx.density(self.G),
            },
            # Adjust into proper format since this is converted into a list for JSON return only
            "graph_degree_distribution": {
                "list_of_unique_degree": unique_degree_list,
                "count_of_unique_degree": unique_degree_count,
                "list_of_in_degree": unique_in_degree_list if nx.is_directed(self.G) else [],
                "count_of_in_degree": unique_in_degree_count if nx.is_directed(self.G) else [],
                "list_of_out_degree": unique_out_degree_list if nx.is_directed(self.G) else [],
                "count_of_out_degree": unique_out_degree_count if nx.is_directed(self.G) else []
            }
        }
        return graph_stats_json

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