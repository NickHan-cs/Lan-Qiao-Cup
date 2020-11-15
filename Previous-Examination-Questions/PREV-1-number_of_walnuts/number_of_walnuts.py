a, b, c = map(int, input().split())
temp_a, temp_b, temp_c = a, b, c
while temp_a % temp_b != 0:
    temp_a, temp_b = temp_b, temp_a % temp_b
d = a * b / temp_b
temp_d = d
while temp_d % temp_c != 0:
    temp_d, temp_c = temp_c, temp_d % temp_c
print(int(d * c / temp_c))
