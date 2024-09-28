
n = 3

arr =[[11, 2, 4],
[4 ,5 ,6],
[10 ,8 ,-12] ]


def diagonalDifference(arr):
    rd = 0
    ld =0 
    for i in range(n):
        rd += arr[i][i]
        ld += arr[i][n-1-i]
     
    return ld -rd
    
print(diagonalDifference(arr))  