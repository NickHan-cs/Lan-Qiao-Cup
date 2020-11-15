x, y, z, x1, y1, z1, p = map(int, input().split())
format_str = '%.' + str(p) + 'f'
print(format_str % (x1 / x + y1 / y + z1 / z))
