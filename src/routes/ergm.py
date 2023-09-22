import networkx as nx
import statsmodels.api as sm

from flask import Blueprint, jsonify

# Create a sample network using networkx
G = nx.Graph()


ergm_page = Blueprint('ergm_page', __name__)
@ergm_page.route('/ergm')
def ergm_return():
    return jsonify({"Ergm Return": "something"}), 200

# Take graph as json ani use that to takeout the statisticss