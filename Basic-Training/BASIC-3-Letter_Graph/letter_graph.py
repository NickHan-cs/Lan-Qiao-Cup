n, m = map(int, input().split(' '))
string = ''
for i in range(m):
    string += chr(65 + i)
for i in range(n):
    print(string)
    string = chr(66 + i) + string[:-1]
