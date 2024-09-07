def bestSum(target,nums,memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0 :
        return None
    shortest = None
    for n in nums:
        remainder = target - n
        result = bestSum(remainder, nums,memo)
        if result is not None:
            combo = result + [n]
            if shortest == None or len(combo) < len(shortest):
                shortest = combo
    memo[target] = shortest
    return shortest


print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(100,[1,2,5,25]))
