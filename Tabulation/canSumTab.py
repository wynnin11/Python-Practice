# Cansum using tabulation
# Does the array contain s subset that can be added to the target

def canSum(target, numbers):
    table = [False] * (target+1)
    table[0] = True
    for i in range(len(table)):
        if table[i] == True:
            for n in numbers:
                if(i+n <= target):
                    table[i+n] = True
    return table[target]

print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(300,[7,14]))

