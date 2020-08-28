n = input()
seq = input().split()
integer = int(input())
ans = -1
for i in range(len(seq)):
    if int(seq[i]) == integer:
        ans = i + 1
        break
print(ans)
