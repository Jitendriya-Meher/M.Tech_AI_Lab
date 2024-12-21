from queue import PriorityQueue
pq = PriorityQueue()

def a_star(graph, start, goal, heuristic):
    
    visted = {}
    
    pq.put( ( heuristic[start], 0, start, []) )
    visted[start] = True

    while ( not pq.empty() ):
        total_cost, path_cost, node, path = pq.get()
        path = path + [node]

        if node == goal:
            return path_cost, path
        else:
            for neighbor, edge_cost in graph[node]:
                if ( neighbor not in visted):
                    new_path_cost = path_cost + edge_cost
                    new_total_cost = new_path_cost + heuristic[neighbor]
                    pq.put( ( new_total_cost, new_path_cost, neighbor, path ) )
                    visted[neighbor] = True

    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0  
}

start, goal = 'A', 'E'
result = a_star(graph, start, goal, heuristic)

if result:
    cost, path = result
    print(f"Lowest-cost path from {start} to {goal}: {path} with cost {cost}")
else:
    print(f"No path found from {start} to {goal}")


# OutPut

# Lowest-cost path from A to E: ['A', 'C', 'D', 'E'] with cost 8