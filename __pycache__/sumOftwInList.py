class Solution(object):
    def twoSum(self, array, target):
       
       num_dic={}
       for i,num in enumerate(array):
           diff=target-num
           if diff in num_dic:
               return[num_dic[diff],i]
           num_dic[num]=i

solution=Solution()   
print(solution.twoSum([2,7,11,15],9))    