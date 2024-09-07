def cansum(target,nums,memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for num in nums:
        remainder = target - num
        if cansum(remainder, nums, memo):
            memo[target] = True
            return True
    return False

print(cansum(7,[2,3]))
print(cansum(7, [5,3,4,7]))
print(cansum(7,[2,4]))
print(cansum(8,[2,3,5]))
print(cansum(300,[7,14]))

