def reverseInteger(number):
    rev=int(str(number)[::-1]) if number>0 else -int(str(-(number))[::-1])
   
    if(rev < -2**31 or rev > 2**31-1):
        return 0       
    return rev


print(reverseInteger(12222))