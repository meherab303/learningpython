def singleNumber(nums):
    # i=0
   
    # while i<len(nums):
    #     if nums.count(nums[i])==1:
    #         return nums[i]
    #     i+=1
    #using bit manipulation -->xor removes duplicates value if duplicate value appear exactly twice.cuz (a xor a=0 ),(0 xor a=a.)So  (a xor a xor a==a)
    # same same hole 0 hobe.
    # result=0
    # for num in nums:
    #     result ^=num
    # return result 
    # using for loop
    for num in nums:
        if nums.count(num)==1:
            return num       
print(singleNumber([4,1,2,1,2,2])) 

#(4 xor 1 xor 2 xor 1 xor 2==4).Here order doesnt matter.firsly (1 xor 1==0).(2 xor 2==0 ) so remaining (4 xor 0 xor 0)==4