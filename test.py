def howSum(target, nums, memo=None):
    if memo is None:
        memo = {}
    
    # Check if the result is already in the memo
    if target in memo:
        return memo[target]
    
    # Base cases
    if target == 0:
        return []
    if target < 0:
        return None
    
    # Try each number in the list
    for n in nums:
        remainder = target - n
        result = howSum(remainder, nums, memo)
        if result is not None:
            memo[target] = result + [n]
            return memo[target]
    
    # If no valid combination is found
    memo[target] = None
    return None

# Testing the function with your test cases
print(howSum(7, [2, 3]))       # Example output: [2, 2, 3] or [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) # Example output: [7] or [4, 3]
print(howSum(7, [2, 4]))       # Expected output: None
print(howSum(8, [2, 3, 5]))    # Example output: [5, 3] or [2, 3, 3]
print(howSum(300, [7, 14]))    # Example output: [14, 14, ..., 14] (21 times)

