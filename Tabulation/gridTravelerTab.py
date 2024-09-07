def gridTraveler(m,n):
    grid = [[0] * n for _ in range(m)]
    grid[0][0] = 1 
    for i in range(m):
        for j in range(n):
            curr = grid[i][j]
            if i+1 < m:
                grid[i+1][j] += curr
            if j+1 < n:
                grid[i][j+1] += curr
    return grid[m-1][n-1]

print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))