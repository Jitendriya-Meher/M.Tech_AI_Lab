from queue import PriorityQueue
pq = PriorityQueue()

def greedy_best_first_search(graph, start, goal, heuristic):

    visted = {}

    pq.put((heuristic[start], start, []))
    visted[start] = True

    while ( not pq.empty()):
        hst_cost, node, path = pq.get()
        path = path + [node]

        if node == goal:
            return path
        else:
            for neighbor in graph[node]:
                if ( neighbor not in visted):
                    pq.put(( heuristic[neighbor], neighbor, path))
                    visted[neighbor] = True
    
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['H'],
    'H': []
}

heuristic = {
    'A': 5,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 5,
    'G': 3,
    'H': 0  
}

start, goal = 'A', 'H'
result = greedy_best_first_search(graph, start, goal, heuristic)

if result:
    print(f"Path from {start} to {goal}: {result}")
else:
    print(f"No path found from {start} to {goal}")


# OutPut

# Path from A to H: ['A', 'B', 'E', 'H']