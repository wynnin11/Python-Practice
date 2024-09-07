def howSum(target, nums,memo=None):
    if memo is None:
	    memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for n in nums:
        remainder = target - n
        result = howSum(remainder, nums,memo)
        if result is not None:
            memo[target] = result + [n]
            return memo[target]
    memo[target] = None
    return None







print(howSum(7,[2,3]))
print(howSum(7, [5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))
