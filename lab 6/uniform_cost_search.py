from queue import PriorityQueue
pq = PriorityQueue()

def uniform_cost_search(graph, start, goal):
    
    pq.put((0, start, []))

    while( not pq.empty() ):
        cost,node,path = pq.get()
        path = path + [node]

        if node == goal:
            return cost , path
        else:
            for neighbor, edge_cost in graph[node]:
                new_cost = cost + edge_cost
                pq.put( (new_cost, neighbor, path) )
    
    return None

graph = {
    'S': [('A', 2), ('B', 4)],
    'A': [('B', 5), ('C', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 3)],
    'D': [('E', 2)],
    'E': []
}

start, goal = 'S', 'E'
result = uniform_cost_search(graph, start, goal)

if result:
    cost, path = result
    print(f"Lowest-cost path from {start} to {goal}: {path} with cost {cost}")
else:
    print(f"No path found from {start} to {goal}")



# OutPut

# Lowest-cost path from S to E: ['S', 'A', 'C', 'E'] with cost 8