def palindrome(number):
    # new_num=str(number)
    # print(new_num[0:])
    
    # if((str(number))=="".join(reversed(str(number)))):
    #     print("palindrome")
    #     return
    result=True if str(number)==str(number)[::-1] else False
    return result
print(palindrome(1222221))