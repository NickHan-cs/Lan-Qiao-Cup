for num in range(100, 1000):
    string = str(num)
    if int(string[0]) ** 3 + int(string[1]) ** 3 + int(string[2]) ** 3 == num:
        print(num)
