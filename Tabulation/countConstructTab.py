# return the number of combinations that can create the target String
# 
#
# m = targetString
# n = len(wordBank)
# Time-complexity O(m^2 + n)
# Space-complextity O(m)

def countConstruct(targetString,wordBank):
    table = [0] * (len(targetString) + 1)
    table[0] = 1 
    for i in range(len(targetString) + 1):
        for word in wordBank:
            if targetString[i:len(word) + i] == word:
                table[i+len(word)] += table[i]
    return table[len(targetString)]


print(countConstruct('purple', ['purp', 'p', 'ur' , 'le', 'purpl']))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo",'rd','ate','t','ska','sk','boar']))
print(countConstruct("enterapotentpot", ["a", "p", "ent",'enter','ot','o','t'])) 
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
"e",
"ee",
"eee",
"eeee",
"eeeee",
"eeeeee"
]))