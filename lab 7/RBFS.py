def rbfs(graph, heuristic, node, goal, g_value, f_limit):
    if node == goal:
        return [node], g_value
    successors = graph[node]
    if not successors:
        return None, float("inf")
    f_values = {}
    for neighbor, cost in successors:
        g = g_value + cost
        f = max(g + heuristic[neighbor], g_value + heuristic[node])
        f_values[neighbor] = f
    while True:
        best = min(f_values, key=f_values.get)
        best_f = f_values[best]
        if best_f > f_limit:
            return None, best_f
        alternative = min((f_values[n] for n in f_values if n != best), default=float("inf"))
        result, best_f = rbfs(graph, heuristic, best, goal, g_value + dict(successors)[best], min(f_limit, alternative))
        if result is not None:
            return [node] + result, best_f

m = 4
n = 4
edges = [(0, 1, 1), (0, 2, 3), (2, 3, 4), (1, 3, 2)]
graph = [[] for _ in range(m)]
for x, y, z in edges:
    graph[x].append((y, z))
heuristic = {}
heuristic_values = [5, 2, 1, 0]
for i in range(m):
    heuristic[i] = heuristic_values[i]
start = 0
goal = 3
f_limit = 5
path, cost = rbfs(graph, heuristic, start, goal, 0, f_limit)
if path:
    print("Path:", path)
    print("Cost:", cost)
else:
    print("No path found within the f_limit.")


# OutPut

# Path: [0, 1, 3]
# Cost: 3