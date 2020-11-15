n = input()
seq = list(map(int, input().split()))
m = int(input())
for i in range(m):
    left, right, k = map(int, input().split())
    tmpSeq = seq[left - 1: right]
    tmpSeq.sort()
    print(tmpSeq[-k])
