import sys

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and flag[x][y] == 0

def dfs(x, y):
    global tmp_sum, min_num, flag, num
    if tmp_sum == all_sum / 2:
        min_num = min(min_num, num)
        return
    for i in range(4):
        xx = x + dir_list[i][0]
        yy = y + dir_list[i][1]
        if is_valid(xx, yy) and tmp_sum + graph[xx][yy] <= all_sum / 2 and num + 1 < min_num:
            flag[xx][yy] = 1
            tmp_sum += graph[xx][yy]
            num += 1
            dfs(xx, yy)
            flag[xx][yy] = 0
            tmp_sum -= graph[xx][yy]
            num -= 1

m, n = map(int, input().split())
graph = []
all_sum = 0
max_num = 0
for i in range(n):
    tmp_list = list(map(int, input().split()))
    graph.append(tmp_list[:])
    all_sum += sum(tmp_list)
    max_num = max(max_num, max(tmp_list))
if all_sum % 2 != 0 or max_num > all_sum / 2:
    print(0)
    sys.exit(0)
dir_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
flag = [[0 for j in range(m)] for i in range(n)]
min_num = m * n
num = 1
tmp_sum = graph[0][0]
flag[0][0] = 1
dfs(0, 0)
if min_num == m * n:
    print(0)
else:
    print(min_num)