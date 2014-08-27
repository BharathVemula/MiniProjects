#Rotating Matrix - rotate a NxN matrix 90 degree clockwise

def populateMatrix(size):
    matrix = []
    count = 1
    for i in xrange(size):
        matrix.append([])
        for j in xrange(size):
            matrix[i].append(count)
            count+=1
    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[i])):
            line += "{:<3d}".format(matrix[i][j])
        print line
    print ""
        
def rotateMatrix(matrix):
    layer = 0
    maxLayer = len(matrix)/2
    size = len(matrix) - 1
    while layer < maxLayer :
        for i in range(layer, size-layer):
            temp = matrix[layer][i]
            #bottom left to top left
            matrix[layer][i] = matrix[size-i][layer]
            #bottom right to bottom left
            matrix[size-i][layer] = matrix[size-layer][size-i]
            #top right to bottom right
            matrix[size-layer][size-i] = matrix[i][size-layer]
            #top left to top right
            matrix[i][size-layer] = temp
        layer += 1
    return matrix

def test():
    for i in range(1, 7) :
        matrix = populateMatrix(i)
        print "before:"
        printMatrix(matrix)
        rotateMatrix(matrix)
        print "after: "
        printMatrix(matrix)

test()
