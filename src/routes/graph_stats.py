# TODOs

# - Use JSON data coming from API Request
# - add node with only selected attributes
# - idenitfy what is regarded as the label for node on addition of node to plot correct network graph
# - Break into Class and method for efficiency

import networkx as nx
import json
import os
import matplotlib.pyplot as plt

from flask import Blueprint, jsonify

# Create a sample network using networkx
G = nx.Graph()


# TODO Use a JSON return in API Request

# Specify JSON Path

script_dir =  os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "test.json")
with open(file_path, "r") as json_data:
    fileData  = json_data.read()
    network_json = json.loads(fileData)

attrs = {}
# Add Nodes
for i in range(len(network_json["nodes"])):
    attribute = network_json["linkAttribute"]
    node_value = json.dumps(network_json["nodes"][i][attribute])
    G.add_node(node_value)
    attrs[node_value] = {}
    for attr in network_json["includedAttribute"]:
        attrs[node_value].update({
                attr: network_json["nodes"][i][attr]
            })

# Add Selected Attributes
nx.set_node_attributes(G, attrs)

# Add Edges
for i in range(len(network_json["links"])):
    source = json.dumps(network_json["links"][i]["source"])
    target = json.dumps(network_json["links"][i]["target"])
    G.add_edge(source, target)

graph_stats_json = {
    "total_edges": nx.number_of_edges(G),
    "total_nodes": nx.number_of_nodes(G),
    "density": nx.density(G),
    "average_clustering_coefficient": nx.average_clustering(G),
    # Only Directed Graphs have strongly connected components
    "number_of_strongly_connected_components": nx.number_strongly_connected_components(G)
        if nx.is_directed(G) else 0,
    "reciprocity": nx.reciprocity(G),
    # Adjust into proper format since this is converted into a list for JSON return only
    "adj_matrix": nx.adjacency_matrix(G).todense().tolist()
}
# nx.draw(G, with_labels=True)
# plt.show()
print(nx.to_edgelist(G))

graph_stats_page = Blueprint('graph_stats', __name__)
@graph_stats_page.route('/graph-stats')
def graph_stats_return():
    return jsonify(graph_stats_json), 200
    return graph_stats_json

    # Take graph as json ani use that to takeout the statisticss