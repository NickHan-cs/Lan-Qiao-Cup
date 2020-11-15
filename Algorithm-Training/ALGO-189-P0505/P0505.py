n = int(input())
num_2 = 0
num_5 = 0
ans = 1
for i in range(2, n+1):
    num = i
    while num % 2 == 0:
        num = num / 2
        num_2 += 1
    while num % 5 ==0:
        num = num / 5
        num_5 += 1
    ans = ans * num % 10
if num_2 > num_5:
    for i in range(num_2 - num_5):
        ans = ans * 2 % 10
else:
    for i in range(num_5 - num_2):
        ans = ans * 5 % 10
print(int(ans))
