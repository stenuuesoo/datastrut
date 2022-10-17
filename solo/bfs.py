graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = [] # Initialize a queue

def bfs(visited, graph, node):
    
    print("Breadth First Search: \n")
    visited.append(node)
    queue.append(node)
    print("Node", node + " is visited and queued.")
    
    while queue:
        currentNode = queue.pop(0)
        print ("Node", currentNode + " is dequeued.")
        
        for childNode in graph[currentNode]:
            if childNode not in visited:
                visited.append(childNode)
                queue.append(childNode)
                print("Child node", childNode + " is visited and queued.")
                
    for visitedNode in visited: print(visitedNode, end=" ")

# Driver Code
bfs(visited, graph, 'A')