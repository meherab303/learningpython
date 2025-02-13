# def seearchInsertionPosition(nums,target):
#     if target not in nums:
#         nums.append(target)
#         nums=sorted(nums)
#     for i in range(len(nums)):
#         if nums[i]==target:
#             return i
        
# print(
# seearchInsertionPosition([1,2,4,5],3))
import bisect

def searchInsertionPosition(nums, target):
    return bisect.bisect_left(nums,target)

print(searchInsertionPosition([1,2,4,5], 5))  

