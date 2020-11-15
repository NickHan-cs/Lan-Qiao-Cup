n = int(input())
pre_line, cur_line = [1], [1]
print(1)
for i in range(1, n):
    pre_line, cur_line = cur_line, [1]
    for j in range(len(pre_line) - 1):
        cur_line.append(pre_line[j] + pre_line[j + 1])
    cur_line.append(1)
    print(' '.join(map(str, cur_line)))
