# given TargetSum 
# given numbers to be summed
# Goal: Find the smallest combination of numbers that add to TargetSum
# Using tabulation

def bestSum(targetSum, numbers):
    table = [None] * (targetSum+1)
    table[0] = [] 
    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    combo = table[i] + [num]
                    if table[i + num] is None or len(combo) <  len(table[i + num]):
                        table[i + num] = combo
    return table[targetSum]

print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[5,3,2]))
print(bestSum(8,[1,4,5]))
print(bestSum(100,[25,1,2,5]))