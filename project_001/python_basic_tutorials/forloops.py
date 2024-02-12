# for item in "python":
#     print(item)   #python

# for i in [1, 2, "asad"]:
#     print(i) #1 ,2 , asad

# for j in range(5):
#     print(j)   #0,1,2,3,4 - LAST number not inluded

# display number of X as in list 

n = [1,1,1,1,5]

for i in range(len(n)) :
    op = ""
    for j in range(n[i]) :
        op += "x"
    print(op)