# howSum(target,nums)
# function that returns an array that contains a combination that sums to target
# Use tabulation
def howSum(target,numbers):
    # Create a table 
    table = [None] * (target+1)
    table[0] = []
    for i in range(target+1):
        if table[i] is not None:
            for n in numbers:
                if i +n <= target:
                    table[i + n] = table[i] + [n]
    return table[target]
print(howSum(7,[3,2]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[3,2,5]))
print(howSum(300,[7,14]))