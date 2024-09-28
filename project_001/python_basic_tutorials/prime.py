


def is_prime(num):
    flag = False
    for x in range(2, num):
        if (num % x) == 0:
            flag = True
            break

    if flag:
        print("Its not a prime")
    else:
        print("its a prime")
        

is_prime(4)




# my_list = [10, 20, 30, 40, 50]

# # Iterate over the list in reverse order using negative indexing
# for i in range(len(my_list) - 1, -1,-1):
#     print(i)
#     print(my_list[i])