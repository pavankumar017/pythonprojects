def timeConversion(s):
    # Write your code here
    lst = s.split(":")
    print(lst)
    if "AM" in s:
        # AM block
        if lst[0] =='12':
            print("ENTERS")
            lst[0] = "00"
    if "PM" in s:
        # PM block
        conv_format = int(lst[0])
        if conv_format >=1 and conv_format < 12:
            add_time =  conv_format + 12
            lst[0] = str(add_time)

    converted_time = lst[0] +":"+lst[1]+":" +lst[2]
    return converted_time
print(timeConversion("1:05:45PM"))