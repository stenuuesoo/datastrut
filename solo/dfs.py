graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # List to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print("Visited Node: " + node, end='\n')
        visited.add(node)
        for neighbor in graph[node]:
            print("Found Child Node of: " + node)
            dfs(visited, graph, neighbor)
    else:
        print("Node " + node + " is already visited.")
    
# Driver Code
print("\nDepth First Search: \n")
dfs(visited, graph, '5')