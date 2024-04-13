len = 8
n1 = 0
n2= 1

arr = []
arr.append(n1)
arr.append(n2)
# [0,1,1,2,3,5,8]
for i in range (2, len):
    sum = n1+n2
    n2 = sum
    n1 = arr[i-1]
    arr.append(sum)
    print(arr)