# A function that returns all the combinations that constructs a targetString
# Using tabulation
# Step 1: Create a table containing arrays, len of the targetString+1 
# Step 2: iterate the length of the targetString
# Step 3: iterate the words in the wordBank
# Step 4: See if the word makes up the target[i:i+len(word)]
# Step 5: if it does append the current table[i] to the arrays found in the table[i+len(word)]
# m = targetString
# n = len(wordBank)
# Time-complexity O(n^m)
# Space-complextity O(n^m)

def allConstruct(targetString,wordBank):
    table = [[] for _ in range(len(targetString)+1)] 
    table[0] = [[]]
    for i in range(len(targetString)):
        for word in wordBank:
            if targetString[i : i + len(word)] == word:
                new_combinations = [sublist + [word] for sublist in table[i]]
                table[i+len(word)].extend(new_combinations)
    return table[len(targetString)]

print(allConstruct('purple', ['purp', 'p', 'ur' , 'le', 'purpl']))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd",'ef','c']))
print(allConstruct("skateboard", ["bo",'rd','ate','t','ska','sk','boar']))
print(allConstruct("aaaaaaaaaaaaaz", ["a", "aa", "aaa",'aaaaa','aaaaaaaa'])) 
