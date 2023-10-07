import networkx as nx
import statsmodels.api as sm

from flask import Blueprint, jsonify
from flask_cors import cross_origin

# class ERGM:
#     def __init__(self):
#         self.G = ''
    
#     def Simulate(self, burn_in, step_size, num_sample):

# Create a sample network using networkx
G = nx.Graph()


ergm_page = Blueprint('ergm_page', __name__)
@ergm_page.route('/ergm')
@cross_origin()
def ergm_return():
    return jsonify({"Ergm Return": "something"}), 200

# Take graph as json ani use that to takeout the statisticss