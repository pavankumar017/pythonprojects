

def removedup(arr):
    new = []
    for i in arr:
        print(i)
        if i not in new :
            new.append(i)
    print(new)      

removedup([1,1,2,3,4,5,3])