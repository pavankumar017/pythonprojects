arr = [1,2,3,4,5,6]
# left = 0 
# right = len(arr)-1
# temp = 0 
# while (left < right):
#     print("onloop")
#     temp = arr[left]
#     arr[left]= arr[right]
#     arr[right]= temp
#     left = left+1
#     right= right-1

# print(arr)







print(arr[::-1])

for i in range(len(arr)-1, -1 , -1):
    print(arr[i])