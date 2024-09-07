# return True/False if the target word can be created using the word bank
# using tabulation 
    # Using a table, size of the targetString
    # table = [[]] * len(targetString + 1)
# m = targetString
# n = len(wordBank)
# Time-complexity O(m^2 + n)
# Space-complextity O(m)
def canConstruct(targetString, wordBank):
    table = [False] * (len(targetString) + 1)
    table[0] = True
    for i in range(len(targetString) + 1 ):
        if(table[i] == True):
            for word in wordBank:
                if targetString[i:i + len(word)] == word:
                    table[i + len(word)] = True
    return table[len(targetString)]

print(canConstruct("abcdef",['ab','abc','cd','def','abcd']))
print(canConstruct("skateboard",['bo','rd','ate','t','ska','sk','boar']))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee'
]))






