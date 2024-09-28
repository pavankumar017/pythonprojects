def bigSorting(unsorted):
    # Write your code here
     
    for i in range(len(unsorted)):
        conv_i = int(unsorted[i])
        n = ""
        print(conv_i)
        for j in range(i+1 , len(unsorted)):
            conv_j = int(unsorted[j])
            print(conv_j)
            if conv_i > conv_j:
                n = str(conv_i)
                unsorted[i] = str(conv_j)
                unsorted[j] = n
            print(unsorted) 
    

bigSorting(["6","12","1","3","10","35"])