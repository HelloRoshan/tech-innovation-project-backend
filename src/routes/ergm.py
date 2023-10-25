# TODO: Add is Fixed parameter and structure zerp s0A parameter

import networkx as nx
import statsmodels.api as sm
import random
import math

from flask import Blueprint, jsonify
from flask_cors import cross_origin

class ERGM:
    def __init__(self, num_vA, is_directed, included_parameters):
        self.G = nx.DiGraph() if is_directed else nx.Graph()
        self.num_vA = num_vA
        self.num_included_parameters = len(included_parameters)
        # This includes the binary cat and continuous type total included/
        self.num_A_parameters = len(included_parameters) # make the count of the sent parameters
         #experimentation so, don't update anything at the moment
        # statistics is updated with parameter proposed value
        # self.parameters = ['Edge', '2Star', 'Triangle']
        self.parameters = [0]* self.num_included_parameters
        self.statistics = [0]* self.num_included_parameters
        self.obsStatistics = [0]* self.num_included_parameters
        self.changestatistics = [0]* self.num_included_parameters
        self.step2changestatistics = [0]* self.num_included_parameters
        # Inside parameter form in mpnet
        self.lambda_var = [2] * self.num_included_parameters
        self.included_index = [0] * self.num_included_parameters

        self.lambda_table = [[0] * self.num_vA for _ in range(self.num_included_parameters)]
        for i in range(self.num_included_parameters):
            for k in range(self.num_vA):
                self.lambda_table[i][k] = (1 - 1 / self.lambda_var[i]) ** k

        # TODO : CORrect
        self.addChangeStats = ''
        self.delChangeStats = ''
        # protected double[] lambda;
        # protected double[][] lambda_table;
    
    def Simulate(self, gm, included_parameters, burn_in=100000, step_size=1000000, num_sample=1000):
        # burn in /step-size/samples
        # file_sim imp

        generated_sim = [['SampleID']]
        # use a predefined parameters for test
        included_parameters = ['Edge', '2Star', 'Triangle']
        generated_sim[0].append(included_parameters)

        # TODO : Add condition for when sample network and sample degree distribution is selected

        for i in range(burn_in):
            self.propose(gm)
            print(i)
            # try use append
            generated_sim.insert(i, [i])

        for i in range(1, num_sample+1):
            for j in range(step_size):
                self.propose(gm)
                generated_sim[i]
                for k in range(len(included_parameters)):
                    # statistics is updated with parameter proposed value
                    generated_sim[i].append(self.statistics(k))
                # Write in new line or new array rather than same
                # TODO : Add condition for when sample network and sample degree distribution is selected
                
        # generate network files after that

        # Simulation done
        
        return ''

    def statistics(self, num):
        return print(num)
    

    def Cstatistics(self, i , j):
        self.G.add_node(i, j)
        # ['Edge', '2Star', 'Triangle']
        # check changes in edge , 2 start, triangle
        self.G.number_of_edges()

    def getEdge(self, i, j):
        return self.G.has_edge(i, j)
    
    def removeEdge(self, i, j):
        self.G.remove_edge(i, j)
    
    def insertEdge(self, i, j):
        self.G.add_edge(i, j)

    def findTotal2Star(self):
        degree_list = list(nx.degree(self.G))
        #Optimized function
        #filter(lambda node_degree: node_degree[1] > 1, degree_list)
        return [node_degree for node_degree in degree_list if node_degree[1] > 1]
    
    def findTotal3Star(self):
        degree_list = list(nx.degree(self.G))
        return [node_degree for node_degree in degree_list if node_degree[1] > 2]

    def propose(self, gm, options):
        graph_nx = {
            "num_vA": 38
        }

        # Strucuture 
        # use options instead of gm

        # Only Network A is considered

        # TODO: define gm and also its parameter
        
        i = random.randint(0, graph_nx.num_vA - 1)
        j = random.randint(0, graph_nx.num_vA - 1)
        # Update if i and j are same
        if i == j:
            i = random.randint(0, graph_nx.num_vA - 1)
            j = random.randint(0, graph_nx.num_vA - 1)
        return self.proposeA(graph_nx, i, j)

    
    def proposeA(self, gm, i, j):
        isAdd = not self.getEdge(i, j)

        if isAdd:
            total = 0.0
            for m in range(self.num_A_parameters):
                self.changestatistics[m] = Cstatistics[m](i, j, self.lambda_var[m], self.lambda_table[m], isAdd, 1, included_index[m])
                total += self.parameters[m] * self.changestatistics[m]

            if math.exp(total) >= random.random():
                for m in range(self.num_A_parameters):
                    self.statistics[m] += self.changestatistics[m]
                
                self.insertEdge(i, j)
                gm.gA.update2path(i, j, isAdd)
                
                return True
        else:
            self.removeEdge(i, j)
            total = 0

            for m in range(self.num_A_parameters):
                self.changestatistics[m] = Cstatistics[m](gm, i, j, self.lambda_var[m], self.lambda_table[m], isAdd, 1, included_index[m])
                total += self.parameters[m] * self.changestatistics[m]

            if math.exp(-total) >= random.random():
                for m in range(self.num_A_parameters):
                    self.statistics[m] -= self.changestatistics[m]
                
                self.update2path(i, j, isAdd)
                return True
            else:
                self.insertEdge(i, j)



    # def your_function_name(s0, gm, i, j, num_A_parameters, parameters, changestatistics, statistics, lambda, lambda_table):

        # k = random.randint(0, gm.num_vA - 1)
        # l = random.randint(0, gm.num_vA - 1)

        # while k == l or (self.getEdge(i, j) == self.getEdge(k, l)):
        #     #TODO: What is getedge doing here
        #     k = random.randint(0, gm.num_vA - 1)
        #     l = random.randint(0, gm.num_vA - 1)


        # if self.getEdge(k, l):
        #     i, k = k, i
        #     j, l = l, j
        #     self.removeEdge(i, j)

        #     total_remove = 0.0
        #     total_add = 0.0

        #     for m in range(self.num_A_parameters):
        #         # implement and see what does the tie change in the graph
        #         self.changestatistics[m] = Cstatistics(m, gm, i, j, lambda[m], lambda_table[m], False, 1, included_index[m])
        #         total_remove += parameters[m] * self.changestatistics[m]

        #     gm.gA.update2path(i, j, False)

        #     for m in range(self.num_A_parameters):
        #         self.step2changestatistics[m] = Cstatistics(m, gm, k, l, lambda[m], lambda_table[m], True, 1, included_index[m])
        #         total_add += parameters[m] * self.step2changestatistics[m]

        #     if math.exp(total_add - total_remove) >= random.random():
        #         for m in range(self.num_A_parameters):
        #             self.statistics[m] += self.step2changestatistics[m] - self.changestatistics[m]
        #         self.insertEdge(k, l)
        #         gm.gA.update2path(k, l, True)
        #         return True

        #     self.insertEdge(i, j)
        #     gm.gA.update2path(i, j, True)

        # else:
        #     isAdd = not self.getEdge(i, j)

        #     if isAdd:
        #         total = 0.0

        #         for m in range(self.num_A_parameters):
        #             self.changestatistics[m] = Cstatistics(m, gm, i, j, lambda[m], lambda_table[m], isAdd, 1, included_index[m])
        #             total += parameters[m] * self.changestatistics[m]

        #         if math.exp(total) >= random.random():
        #             for m in range(self.num_A_parameters):
        #                 self.statistics[m] += self.changestatistics[m]

        #             self.insertEdge(i, j)
        #             gm.gA.update2path(i, j, isAdd)
        #             return True

        #     else:
        #         self.removeEdge(i, j)
        #         total = 0.0

        #         for m in range(self.num_A_parameters):
        #             self.changestatistics[m] = Cstatistics(m, gm, i, j, lambda[m], lambda_table[m], isAdd, 1, included_index[m])
        #             total += parameters[m] * self.changestatistics[m]

        #         if math.exp(-total) >= random.random():
        #             for m in range(self.num_A_parameters):
        #                 self.statistics[m] -= self.changestatistics[m]
        #             return True
        #         else:
        #             self.insertEdge(i, j)
        # return False

# ergm_page = Blueprint('ergm_page', __name__)
# @ergm_page.route('/ergm')
# @cross_origin()
# def ergm_return():
#     simulate = ERGM(38)
#     simulate.Simulate()
#     return jsonify({"Ergm Return": "something"}), 200

# Take graph as json ani use that to takeout the statisticss
included_parameters = ['Edge', '2Star', 'Triangle']
isdirectedgraph = False
simulate = ERGM(38, isdirectedgraph, included_parameters)
simulate.Simulate()