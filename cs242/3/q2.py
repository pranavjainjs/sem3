n = 0          # counts the number of steps
inversionCount = 0       # inversion count of the matrix

### taking input

# initial grid is read from command line
initialGrid = []    

print("enter 9 numbers in the initial grid")
for i in range(3):
    l = []
    for j in range(3):
        l.append(int(input()))
    initialGrid.append(l)


# final grid is read from command line
finalGrid = []


print("enter 9 numbers in the final grid")
for i in range(3):
    l = []
    for j in range(3):
        l.append(int(input()))
    finalGrid.append(l)


# returns a 1D list from a 2D list
def traverse(mat):
    map = []
    for i in range(3):
        for j in range(3):
            map.append(mat[i][j])
    return map


# shifts 0 to bottom right
def botRgtZero(mat):
    p, q = where(0, mat)
    for i in range(p, 2):
        down(mat)
    for i in range(q, 2):
        right(mat)


# prints a 2D nxn matrix in n rows and n columns
def p2d(mat):
    for r in mat:
        for c in r:
            print(c, end=" ")
        print()


# the solve function goes here
def Solve(mat):
    # trivial case(s)
    # if inversion count is 0, it means that the list is in ascending order (except for 0)
    # hence, solving the problem is trivial
    if inversionCount == 0 and mat[2][2] == 0:
        return
    elif inversionCount == 0 and mat[2][0] == 0:
        right(mat)
        right(mat)
        return
    elif inversionCount == 0 and mat[2][1] == 0:
        right(mat)
        return
    elif inversionCount == 2 and mat[2][2] == 6 and mat[1][2] == 0:
        down(mat)
        return

    # the problem is essentially solved here
    else:
        centreZero(mat)
        One(mat)
        Two(mat)
        Three(mat)
        Four(mat)
        Five(mat)
        SixSevenEight(mat)


# determines if the given matrices are solvable
def isSolvable(mat):
    global inversionCount
    list = []
    for i in range(3):
        for j in range(3):
            list.append(mat[i][j])

    # computing the inversion count 
    for i in range(9):
        for j in range(i, 9):
            if list[i] > list[j] and list[j] != 0:
                inversionCount += 1

    # the given matrices are solvable if and only if inversion count is even
    if inversionCount % 2 == 1:
        print("Goal configuration cannot be achieved from given configuration\n")
        exit()
    elif inversionCount == 0 and list[8] == 0:
        print("Given configuration is the goal configuration\n")
    else:
        print("Goal configuration can be achieved from given configuration\n")
        return


# re-tracing the steps to shift Zero at its desired position
def backTracking(mat, p, q):
    global n
    p = 2 - p
    q = 2 - q
    for i in range(0, q):
        left(mat)
    for i in range(0, p):
        up(mat)


# returns the index of an element in a matrix
def where(x, mat):
    for r in range(3):
        for c in range(3):
            if mat[r][c] == x:
                return r, c
    return -1, -1


# shift 0 to left
def left(mat):
    global n
    n = n + 1
    x, y = where(0, mat)
    mat[x][y], mat[x][y - 1] = mat[x][y - 1], mat[x][y]
    p2d(mat)
    print()


# shift 0 to right
def right(mat):
    global n
    n = n + 1
    x, y = where(0, mat)
    mat[x][y], mat[x][y + 1] = mat[x][y + 1], mat[x][y]
    p2d(mat)
    print()


# shift 0 to upwards
def up(mat):
    global n
    n = n + 1
    x, y = where(0, mat)
    mat[x][y], mat[x - 1][y] = mat[x - 1][y], mat[x][y]
    p2d(mat)
    print()


# shift 0 to downwards
def down(mat):
    global n
    n = n + 1
    x, y = where(0, mat)
    mat[x][y], mat[x + 1][y] = mat[x + 1][y], mat[x][y]
    p2d(mat)
    print()


# shift 0 to center
def centreZero(mat):
    p, q = where(0, mat)
    global n

    if p == 1 and q == 0:
        mat[1][q], mat[1][1] = mat[1][1], mat[1][q]
        p2d(mat)
        print()
        n += 1
    elif p != 1 and q == 1:
        mat[p][1], mat[1][1] = mat[1][1], mat[p][1]
        p2d(mat)
        print()
        n += 1
    elif q == 2:
        left(mat)
        centreZero(mat)
    elif p == 2:
        up(mat)
        centreZero(mat)
    elif p == 0 and q == 0:
        right(mat)
        down(mat)
    return


# shifts 1 to index (0,0)
def One(mat):
    p, q = where(1, mat)
    # print(p,q)
    if p == 0 and q == 0:
        return
    elif p == 0 and q == 1:
        left(mat)
        up(mat)
        right(mat)
        down(mat)
    elif p == 1 and q == 0:
        up(mat)
        left(mat)
        down(mat)
        right(mat)
    elif p == 2 and q == 0:
        left(mat)
        down(mat)
        right(mat)
        up(mat)
        One(mat)
    elif p == 0 and q == 2:
        up(mat)
        right(mat)
        down(mat)
        left(mat)
        One(mat)
    elif p == 2 and q == 1:
        down(mat)
        left(mat)
        up(mat)
        right(mat)
        One(mat)
    elif p == 1 and q == 2:
        # print("gello")
        right(mat)
        up(mat)
        left(mat)
        down(mat)
        One(mat)
    elif p == 2 and q == 2:
        right(mat)
        down(mat)
        left(mat)
        up(mat)
        One(mat)
    return


# shifts 2 to index (0,1)
def Two(mat):
    p, q = where(2, mat)
    if p == 0 and q == 1:
        return
    elif p == 1 and q == 0:
        left(mat)
        down(mat)
        right(mat)
        up(mat)
        Two(mat)
    elif p == 2 and q == 0:
        down(mat)
        left(mat)
        up(mat)
        right(mat)
        Two(mat)
    else:
        while p != 0 or q != 1:
            down(mat)
            right(mat)
            up(mat)
            up(mat)
            left(mat)
            down(mat)
            p, q = where(2, mat)
    return


# shifts 3 to index (0,2)
def Three(mat):
    p, q = where(3, mat)
    if p == 0 and q == 2:
        return
    else:
        while p != 1 or q != 0:
            left(mat)
            down(mat)
            right(mat)
            right(mat)
            up(mat)
            left(mat)
            p, q = where(3, mat)
    left(mat)
    up(mat)
    right(mat)
    down(mat)
    right(mat)
    up(mat)
    left(mat)
    left(mat)
    down(mat)
    right(mat)
    return


# shifts 4 to index (1,0)
def Four(mat):
    p, q = where(4, mat)
    if p == 1 and q == 0:
        return
    centreZero(mat)
    while p != 1 or q != 0:
        left(mat)
        down(mat)
        right(mat)
        right(mat)
        up(mat)
        left(mat)
        p, q = where(4, mat)


# shifts 5 to index (1,1)
def Five(mat):
    p, q = where(5, mat)
    # print(p, q)
    if p == 1 and q == 1:
        return
    elif p == 2 and q == 0:
        left(mat)
        down(mat)
        right(mat)
        up(mat)
        left(mat)
        down(mat)
        right(mat)
        right(mat)
        up(mat)
        left(mat)
        left(mat)
        down(mat)
        right(mat)
        up(mat)
    else:
        while p != 1 or q != 2:
            down(mat)
            right(mat)
            if mat[1][1] == 5:
                return
            up(mat)
            left(mat)
            p, q = where(5, mat)
    return


# places 6,7,8 to index (1,2), (2,0) and (2,1) respectively
def SixSevenEight(mat):
    p, q = where(6, mat)
    if p == 1 and q == 2:
        if mat[2][0] == 0:
            right(mat)
            right(mat)
        elif mat[2][1] == 0:
            right(mat)
        return
    elif p == 2 and q == 2:
        right(mat)
        down(mat)
        return
    elif p == 2 and q == 0:
        right(mat)
        down(mat)
        left(mat)
        left(mat)
        up(mat)
        right(mat)
        down(mat)
        right(mat)
        up(mat)
        left(mat)
        left(mat)
        down(mat)
        right(mat)
        right(mat)
    elif p == 2 and q == 1:
        right(mat)
        down(mat)
        left(mat)
        left(mat)
        up(mat)
        right(mat)
        right(mat)
        down(mat)
        left(mat)
        up(mat)
        left(mat)
        down(mat)
        right(mat)
        right(mat)
    return


s, t = where(0, finalGrid)

# displaying the inputs and their counterparts obtained after shifting Zero to bottom right 

print("\nthe initial grid is-")
p2d(initialGrid)
print()
print("initial grid on shifting 0 to bottom right corner")
botRgtZero(initialGrid)


print("\nthe final grid is-")
p2d(finalGrid)
print()
print("final grid on shifting 0 to bottom right corner")
botRgtZero(finalGrid)


# used while mapping 
# mapped elements of initial grid to successor of their in this list 
mapf = traverse(finalGrid) 


# Updating the values in initial grid to their image in mapping
print("\nthe mapping is-")
for i in range(3):
    for j in range(3):
        if initialGrid[i][j] != 0:
            initialGrid[i][j] = mapf.index(initialGrid[i][j])+1
            print(initialGrid[i][j], "--->", mapf.index(initialGrid[i][j])+1)
print()

print("the mapped matrix is -")
p2d(initialGrid)
print()

isSolvable(initialGrid)


Solve(initialGrid)

# replacing the numbers with their pre images in mapping 

print("elements of matrix are replaced by their pre images in mapping")
for i in range(3):
    for j in range(3):
        if initialGrid[i][j] != 0:
            initialGrid[i][j] = mapf[initialGrid[i][j] - 1]

p2d(finalGrid)
print()

# backTracking Zero to its place in the final grid
backTracking(finalGrid, s, t)

# subtracting the extra steps counted in line botRgtZero(finalGrid)
# adding two steps of replacing with images and pre image
n = n-(4-s-t)+2   

print("\nGoal configuration can be achieved in ", n, " steps.\n")
