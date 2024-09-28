
b = '0100101010'

def beautifulBinaryString(b):
    # Write your code here
    nth_index = 0 
    count = 0 
    while nth_index >=0 :
        nth_index = b.find("010")
        if nth_index == -1:
            break
        print(nth_index)
        print(b[nth_index])
        if b[nth_index] == '0':
            print("inloop")
            b = b[:nth_index] + '1' + b[nth_index + 1:]
            count = count+1
        else:
            b = b[:nth_index] + '0' + b[nth_index + 1:]
            count = count +1
        
        print(count)

        print(b)

beautifulBinaryString(b)