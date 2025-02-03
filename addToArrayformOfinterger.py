# num = [1,2,0,0]
# num_string=list(map(str,num))
# k = 34
# new_str=""
# for x in num_string:
#     new_str+=x
# k+=int(new_str)
# new_k=str(k) 
# new_arr=[]
# for i in range(len(new_k)):
#     new_arr.append(new_k[i])

# better approach

num = [1,2,0,0]
k=34
new_num=list(map(int,str(int("".join(list(map(str,num))))+k)))
print (new_num ) 