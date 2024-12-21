def iterative_deepening_a_star_rec(graph, heuristic, node, goal, distance, threshold):

    print("Visiting Node " + str(node))

    if node == goal:
        return True, distance

    curr_threshold = distance + heuristic[node]

    if( curr_threshold > threshold ):
        return False, curr_threshold
    
    new_threshold = float("inf")

    for neighbor, weight in graph[node]:
        found,nei_threshold = iterative_deepening_a_star_rec(graph, heuristic, neighbor, goal, distance + weight, threshold)
        if found == True:
            return True, nei_threshold
        elif nei_threshold < new_threshold:
            new_threshold = nei_threshold

    return False, new_threshold

def iterative_deepening_a_star(graph, heuristic, start, goal):
    threshold = heuristic[start]
    while True:
        print("Iteration with threshold: " + str(threshold))
        found , answer = iterative_deepening_a_star_rec(graph, heuristic, start, goal, 0, threshold)
        if found == True:
            print("Found the node we're looking for!")
            return answer
        elif answer == float("inf"):
            print(f"The Node {goal} is not preset in the Graph!")
            return -1
        else:
            threshold = answer

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3), ('G', 6)],
    'D': [],
    'E': [('H', 3)],
    'F': [],
    'G': [('H', 1)],
    'H': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 6,
    'E': 2,
    'F': 5,
    'G': 3,
    'H': 0  
}

start, goal = 'A', 'H'
iterative_deepening_a_star(graph, heuristic, start, goal)


# OutPut

# Iteration with threshold: 7
# Visiting Node A
# Visiting Node B
# Visiting Node D
# Visiting Node E
# Visiting Node C
# Iteration with threshold: 8
# Visiting Node A
# Visiting Node B
# Visiting Node D
# Visiting Node E
# Visiting Node H
# Found the node we're looking for!