import time
def canConstruct(target, letters, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for letter in letters:
        if target.startswith(letter):
            suffix = target[len(letter):]
            if canConstruct(suffix,letters,memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

start_time = time.time()

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"] ))
print(canConstruct("skateboard", ["bo","rd", "ate", "t", "ska", "sk",
"boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
"e",
"ee"
"eee"
"eeee"
"eeeee"
"eeeeee"
]))
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
