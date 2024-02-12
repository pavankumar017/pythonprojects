def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
        print(f'mid = {mid})')
 
        # Dividing the array elements
        L = arr[:mid]
        print(L)
        # Into 2 halves
        R = arr[mid:]
        print(R)
        # Sorting the first half
        mergeSort(L)
       
        # Sorting the second half
        mergeSort(R)
        

arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)