# number = "123"
# digits = list(map(int, number))
# print(digits)


# def plusOne(array):
#     new_strr=""
#     for elem in array:
#         new_strr+=str(elem)
#     return list(map(int, (str(int(new_strr)+1))))
# def plusOne(digits):
#     num = int("".join(map(str, digits))) + 1
#     return list(map(int, str(num)))
def plusOne(digits):
    new_num=int("".join(map(str, digits)))+1 
    return new_num 

print(plusOne([9]))         

#  if digit[len(digits)-1]==9
    
    #     return 1
    # else: