for num in range(1000, 10000):
    string = str(num)
    if string[0] == string[3] and string[1] == string[2]:
        print(num)
