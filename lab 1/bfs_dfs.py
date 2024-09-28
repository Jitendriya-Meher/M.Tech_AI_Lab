
graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6','7'],
  '4' : [],
  '5' : [],
  '6' : [],
  '7' : []
}

def notVis(arr, node):
    for val in arr:
        if( val == node):
            return False
    return True

def bfs(graph,root):
    visited = [] 
    queue = []

    visited.append(root)
    queue.append(root)

    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr, end=" ")

        for nei in graph[curr]:
            if ( notVis(visited, nei) ):
                visited.append(nei)
                queue.append(nei)


def dfs(graph,vis,node):
    vis.append(node)
    print(node,end=" ")

    for nei in graph[node]:
        if( notVis(vis, nei) ):
            dfs(graph,vis,nei)

print("BFS = ",end="")
bfs( graph ,'1')
print()

vis = []
print("DFS = ",end="")
dfs(graph,vis,'1')
print()
