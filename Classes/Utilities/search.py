class Search():
    def __init__(self):
        return 
    
    def dfs(self, node, dependencies, visited, dependency_analysis):
        visited.add(node)
        for neighbor in dependencies.get(node, []):
            if neighbor not in visited:
                dependency_analysis[node].add(neighbor)
                self.dfs(neighbor, dependencies, visited, dependency_analysis)