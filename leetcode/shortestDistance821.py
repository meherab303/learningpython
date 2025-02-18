def shortestDistance(s,c):
    indexed_list=[ i for i,char in enumerate(s) if char==c]
    # for i in range(len(s)):
    #     if s[i]==c:
    #         indexed_list.append(i)
    final_index_list=[]
    print(indexed_list)
    i=0
    while i<len(s):
        small_index=abs(i-indexed_list[0])
        print("f",small_index)
        for index in indexed_list:
            if(abs(i-index)<small_index):
                small_index=abs(i-index)
                print("l",small_index)
                
        final_index_list.append(small_index)
        i+=1

    return final_index_list





print(shortestDistance("loveleetcode","e"))