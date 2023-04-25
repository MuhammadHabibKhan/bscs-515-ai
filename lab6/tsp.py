# implementing TSP with naive solution 

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def tsp(g):
    nodeNumber = len(graph)
    nodeList = []
    # generating a generic permutations for n-1 nodes. (n-1 since starting point (0) is fixed)
    for node in range(nodeNumber):
        if node != 0:
            nodeList.append(node)
    permuteList = permute(nodeList)
    print(permuteList)
    
    pathList = []
    for path in permuteList:
        subpath = []
        prevNode = 0 # start with previous node = 0 as we start with 0 and 0th row tells us weight to each node
        for node in range(len(path)):
            nodePos = path[node] # tells us which element to pick from each row 
            nodeWeight = g[prevNode][nodePos] # prev node here since first time 0, then to see weight of where we are going, we need to
            # the row where we were previously since it contains the weight to each node
            prevNode = nodePos
            subpath.append(nodeWeight)
        #print(subpath)
        lastNode = g[prevNode][0] # appending final distance of going back to 0 from final node
        subpath.append(lastNode)
        pathList.append(subpath)

    print(pathList)

    weightList = []
    for pathWeights in pathList:
        weightList.append(sum(pathWeights))
    print(weightList)

    minimumWeight = min(weightList)
    minIndex = weightList.index(minimumWeight)

    minPath = permuteList[minIndex]
    minPath.insert(0,0)
    minPath.append(0)

    for a in range(len(minPath)):
        minPath[a] += 1

    # prints only first minimum path but can be easily changed through a custom implementation of min function
    print(str(minPath) + ' ----> ' + str(minimumWeight))


def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        n = nums[i]
        rest = nums[:i] + nums[i+1:]
        for permutation in permute(rest):
            result.append([n] + permutation)
    return result

tsp(graph)