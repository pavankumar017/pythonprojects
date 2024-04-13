string = "ABCDCDC"
sub_string = "CDC"
count=0
start=0
for i in range(len(string)):
    j=string.find(sub_string,start)
    print(j)
    if j!=-1:
        start=j+1
        count+=1

# print(count)