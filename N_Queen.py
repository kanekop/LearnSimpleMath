import itertools
import math

N = 8
def QueenEffect(grid, qx, qy):
    # up-left, up-right, down-left, down-right
    x = (-1, 1, -1, 1)
    y = (1, 1, -1, -1)
    
    if grid[qx][qy] == ".":
        return False
    for i in range(1,N):
        for j in range(4):
            if 0 <= qx+x[j]*i <= N-1 and 0 <= qy+y[j]*i <= N-1:
                grid[qx+x[j]*i][qy+y[j]*i] = "."
    
    return True

def printgrid():
    for i in grid:
        print("".join(i))

print(math.factorial(N))
l = [i for i in range(N)]
ctr = 0
P = [i for i in itertools.permutations(l)]

# diagonal check
print(len(P))
for i in range(len(P)):
    p = P[i]
    grid = [["X"]*N for _ in range(N)]
    good = True
    for i in range(N):    
        if QueenEffect(grid, i, p[i]):
            grid[i][p[i]] = "Q"
        else:
            good = False
            break
    if good:
        printgrid()
        ctr += 1
print(ctr)
