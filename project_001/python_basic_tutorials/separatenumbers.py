# def separateNumbers(s):
#     for i in range(1, len(s) // 2 + 1):
#         first_num = int(s[:i])
#         current_num = first_num
#         current_str = str(first_num)

#         while len(current_str) < len(s):
#             current_num += 1
#             print(current_num)
#             current_str += str(current_num)
#             # print(current_str)

#         if current_str == s:
#             print(f"YES {first_num}")
#             return

#     print("NO")


def separateNumbers(s):
    # Write your code here
    # first you iterate with 1 digit , 2 digit , 3 digir - for these we use half of string 
    print(len(s)//2+1)
    for i in range(1, len(s)//2+1):
        firstnum = int(s[:i])
        curnum = firstnum
        curstr = str(curnum)
        
        # now i check whether the lenth of string is less than given or not and it loops till the length of string is same 
        while len(curstr) < len(s):
            curnum = curnum +1
            curstr = curstr+ str(curnum)
            
        if curstr == s:
            print(f'Yes {firstnum}')
            return
        
    print("No")


separateNumbers('1234')

