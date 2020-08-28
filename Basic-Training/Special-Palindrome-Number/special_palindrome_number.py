n = int(input())
for num in range(10000, 100000):
    string = str(num)
    if string[0] == string[4] and string[1] == string[3] and n == 2 * (int(string[0]) + int(string[1])) + int(
            string[2]):
        print(num)
for num in range(100000, 1000000):
    string = str(num)
    if string[0] == string[5] and string[1] == string[4] and string[2] == string[3] and n == 2 * (
            int(string[0]) + int(string[1]) + int(string[2])):
        print(num)
