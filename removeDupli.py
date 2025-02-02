def dupliRemove(nums):
        # arr=[]
        
        # for x in nums:
        #     if not x in arr:
        #         arr.append(x)
           
                    
        # return len(arr) 

    # two pointer array
        i=0
        for j in range(1,len(nums),1):
                if nums[i]!=nums[j]:
                        i+=1
                        nums[i]=nums[j]

        return i+1               
           
        
        
        
print(dupliRemove([1,1,2,2,3,3]))