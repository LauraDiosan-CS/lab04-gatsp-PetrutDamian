def evaluateTsp(path,matrix):
    cost = 0
    for i in range(0,len(path)-1):
        cost += matrix[path[i]][path[i+1]]
    cost += matrix[path[-1]][path[0]]
    return cost