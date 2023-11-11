#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
   def twoSum(self,nums,target):
    s=len(nums)
    for i in range(s):
        for j in range(i+1,s):
            if nums[i]+nums[j]==target:
               return [i,j]
        
