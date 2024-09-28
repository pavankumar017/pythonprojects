a = [1,2,3,0,0,0]
b = [2, 5, 6]
m = 3 
n= 3
i = m-1
j = n-1
print(i, j)
# should merge and it should be srte in a 
k = (m + n) -1
while i >=0 and j >=0 :
    if a[i] > b[j]:
        a[k] = a[i]
        print(i , j , a)
        i = i-1
       
    else:
        a[k]= b[j]
        print(i, j ,a)
        j = j-1
    k = k-1

print(a)


