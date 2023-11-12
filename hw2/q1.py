def rangeQuery(C, a, b, i, j):
    m = (j - i + 1) // 2
    l = 0
    r = 0
    if a <= C[m]:
        l = rangeQuery(C, a, b, i, m)
    else:
        l = rangeQuery(C, a, b, m + 1, j)
    if b < C[m]:
        r = rangeQuery(C, a, b, i, m)
    else:
        r = rangeQuery(C, a, b, m + 1, j)

print(rangeQuery([2, 3, 4, 4, 4, 5, 6, 8], 4, 6, 0, 7))
