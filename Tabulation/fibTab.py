def fibTab(n):
    table = [0] * (n + 1)
    table[1] = 1 
    for i in range(n):
        table[i+1] += table[i]
        table[i+2] += table[i]
    return table[n]
fibTab(7)