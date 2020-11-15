n = int(input())
cross = [['.' for j in range(4*n+5)] for i in range(4*n+5)]
for i in range(2*n, 2*n+5):
    cross[2*n+2][i] = '$'
    cross[i][2*n+2] = '$'
for i in range(1, n+1):
    for j in range(2*i, 4*n+5-2*i):
        cross[2*i-2][j] = '$'
        cross[4*n+6-2*i][j] = '$'
        cross[j][2*i-2] = '$'
        cross[j][4*n+6-2*i] = '$'
    cross[2*i][2*i] = '$'
    cross[2*i-1][2*i] = '$'
    cross[2*i][2*i-1] = '$'
    
    cross[2*i][4*n+4-2*i] = '$'
    cross[2*i-1][4*n+4-2*i] = '$'
    cross[2*i][4*n+5-2*i] = '$'
    
    cross[4*n+4-2*i][2*i] = '$'
    cross[4*n+4-2*i][2*i-1] = '$'
    cross[4*n+5-2*i][2*i] = '$'
    
    cross[4*n+4-2*i][4*n+4-2*i] = '$'
    cross[4*n+4-2*i][4*n+5-2*i] = '$'
    cross[4*n+5-2*i][4*n+4-2*i] = '$'
for i in range(4*n+5):
    for j in range(4*n+5):
        print(cross[i][j], end='')
    print()
