n, m = map(int, input().split())
graph = [[' 0' for j in range(m)] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x-1][i] = ' 1'
    graph[y-1][i] = '-1'
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()
