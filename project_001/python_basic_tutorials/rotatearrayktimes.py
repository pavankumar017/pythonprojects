# given a array = [2,4,3,5,6,3,7]
# rotate k times , K=3 
# o/p = [6,3,7,2,4,3,5]

k = 4
arr = [2,4,3,5,6,3,7]
length_array = len(arr)
arr1 = arr[0:length_array-k]
print(arr1)
arr2 = arr[length_array-k:]
print(arr2)
result = arr2 +arr1
print(result)

# o/p
"""[2, 4, 3]
[5, 6, 3, 7]
[5, 6, 3, 7, 2, 4, 3]"""