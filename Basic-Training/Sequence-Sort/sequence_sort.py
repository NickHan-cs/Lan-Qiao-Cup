n = input()
seq = list(map(int, input().split()))
seq.sort()
print(' '.join(map(str, seq)))
