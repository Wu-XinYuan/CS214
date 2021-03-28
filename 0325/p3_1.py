n = 5
schedule = [[0]*n for _ in range(n-1)]
for i in range(n-1):
    for j in range(n):
        schedule[i][j] = (i + j + 2) % n
print(schedule)
