def allConstruct(target,wordbank,memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    res = [] 
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixways = allConstruct(suffix, wordbank,memo)
            targetways = [[word, *way] for way in suffixways]
            res.extend(targetways)

    memo[target] = res
    return res

print(allConstruct('purple',['purp','p','ur','le','purpl']))
print(allConstruct("abcdef", ["ab",
"abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct("skateboard", ["bo",
"rd", "ate", "t", "ska", "sk",'boar']))
print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa","aaa", "aaaa",'aaaaa']))