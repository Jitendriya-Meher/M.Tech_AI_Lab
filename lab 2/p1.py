def cleanRoom( room , i, j, rows, cols ,vis):

    # out of room 
    if ( i>=rows or j>=cols or i<0 or j<0):
        return
    
    # skip the already visited room 
    if( vis[i][j] == 1):
        return
    
    vis[i][j] = 1
    
    if( room[i][j] == 'd'):
        room[i][j] = 'c'
    
    # go up 
    cleanRoom( room, i+1, j, rows, cols, vis)
    # go right 
    cleanRoom( room, i, j+1, rows, cols, vis)
    # go down 
    cleanRoom( room, i-1, j, rows, cols, vis)
    # go left 
    cleanRoom( room, i, j-1, rows, cols, vis)

room = [
    ['d','c','d','c','d'],
    ['d','c','d','c','d'],
    ['d','c','d','c','d'],
    ['d','c','d','c','d'],
    ['d','c','d','c','d']
]

rows = len(room)
cols = len(room[0])

vis = []

for i in range(rows):
    temp = []
    for j in range(cols):
        temp.append(temp)
    vis.append(temp)

# print(f"rows : {rows} , cols : {cols}")

print("Before Cleaning")
print(room)

cleanRoom( room, 2,2,rows,cols, vis)

print("After Cleaning")
print(room)