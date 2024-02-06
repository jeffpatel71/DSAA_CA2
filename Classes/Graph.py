# import networkx as nx
# import matplotlib.pyplot as plt

class Graph:
    def __init__(self, table):
        self.__table = table

    def visualize_dependency_graph(self):
        print('')
        for variable, dependencies in self.__table.items():
            if dependencies == set():
                print(f'{variable} does not have dependencies in current variables')
            else:
                print(f"{variable} has dependencies in:", ", ".join(dependencies))
        print('')


#     def visualize_hashtable_graph(self):
#         # Create a directed graph
#         G = nx.DiGraph()

#         # Add nodes and edges to the graph
#         for key, values in self.__table.items():
#             for value in values:
#                 G.add_edge(value, key)

#         # Plot the graph
#         pos = nx.spring_layout(G)  # positions for all nodes
#         nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
#         plt.title("Variable Dependency Graph")
#         plt.show()