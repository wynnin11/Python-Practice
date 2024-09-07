#get from the top left to the bottom right corner
# find all paths
# S -> E
# gridtraveler(2,3)
# right, right, down

def gridtraveler(r,c,memo = {}):
    key = str(r) + "," + str(c)
    if key in memo:
        return memo[key]
    if r == 0 or c == 0:
        return 0
    if r == 1 and c == 1:
        return 1
    memo[key] =  gridtraveler(r-1,c,memo) + gridtraveler(r,c-1,memo)
    return memo[key]
print(gridtraveler(18,18))
