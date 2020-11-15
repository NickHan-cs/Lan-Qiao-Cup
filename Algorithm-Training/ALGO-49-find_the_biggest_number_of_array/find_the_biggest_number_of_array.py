n = int(input())
a = list(map(int, input().split()))
max_value = a[0]
max_pos = 0
for i in range(1, len(a)):
    if a[i] > max_value:
        max_value = a[i]
        max_pos = i
print(max_value, max_pos)
