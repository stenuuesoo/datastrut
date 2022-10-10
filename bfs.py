graph = {
  '1' : ['30','91'],
  '5' : ['21', '44'],
  '7' : ['82'],
  '6' : [],
  '15' : ['8'],
  '22' : []
}

visited = [] # List to keep track of visited nodes.

def bfs(visited, graph, node):
    visited.append(node)
    print("Visited: ", node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.append(neighbour)
            print("Visited neighbour: ", neighbour)

def main():
    print("Breadth First Search: \n")
    for i in graph: bfs(visited, graph, i)
    print("\nVisited nodes in order:")        
    for i in visited: print(i, end=" ")

if __name__ == "__main__": main()