# min and max sum of array
# https://www.hackerrank.com/challenges/mini-max-sum/problem


# so the trick is after sorting the largest number goes to last and smallestto first - 
# Hence for minimum sum we need to add all numbers except last one and for maximum sum we need to add all numbers except first one.
def miniMaxSum(arr):
    arr.sort()
    minsum = 0
    maxsum = 0
    for i in range(0, len(arr)-1):
        minsum += arr[i]
    for i in range(1, len(arr)):
        maxsum += arr[i]
    print(minsum, maxsum)