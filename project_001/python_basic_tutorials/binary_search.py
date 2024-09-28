arr1 =  [20,12,36,45,51,67,87]
n = 67
arr1.sort()


def search(arr, n):
    low = 0
    high = len(arr)+1
    mid = 0 
    while (low <high):
        mid = (low + high) // 2
        print(mid)

        if (arr[mid] == n):
            return mid

        elif (arr[mid]< n):
            low = mid

        elif (arr[mid] > n):
            high = mid

a = search([12,20,36,45,51,67], 67)

print(f'{"the index is "} {a}')