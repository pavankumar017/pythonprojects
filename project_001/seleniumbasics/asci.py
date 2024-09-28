def funnyString(s):
    # Write your code here

    # def asci_conv(str):
    #     arr = []
    #     print(str)
    #     for i in range(0,len(str)):
    #         print(str[i])
    #         a = ord(str[i])
    #         arr.append(a)
    #     return arr  
            
    # asci_straight = asci_conv(s)
    # asci_reverse = asci_conv(s[::-1])
    # print(asci_straight)
    # print(asci_reverse)
    
    # def check_funny(asci_list):
    #     flag = []
    #     for i in range(0,len(asci_list)-1):
    #         if asci_list[i] - asci_list[i+1] ==1:
    #             flag = True
    #         else:
    #             flag = False
            
    #     print(flag)
    #     # if False in flag:
    #     #     print("Not funny")
    #     # else:
    #     #     print("Funny")

    # check_funny(asci_straight)

    diff = [
        abs(ord(s[i]) - ord(s[i + 1]))
        for i in range(len(s) - 1)
    ]
    if diff == diff[::-1]:
        return 'Funny'
    return 'Not Funny'



funnyString("acxz")