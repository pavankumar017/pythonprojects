# arr =   [2, 5, 8,6, 7, 3,1]
# sort the array 


def sort (arr): 
    arr1 = []
    n =0 
    for i in range(0, len(arr)):
        for j in range(i+1 , len(arr)):
            if (arr[i]> arr[j]):
                n = arr[i]
                arr[i]=  arr[j]
                arr[j] = n
                print( i )
                print( j)
                print(arr)

    



sort([2, 5, 8,6, 0, 3,1])