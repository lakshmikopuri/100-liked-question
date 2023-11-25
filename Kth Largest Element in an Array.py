#Kth Largest Element in an Array
#Given an integer array nums and an integer k, return the kth largest element in the array.Note that it is the kth largest element in the sorted order, not the kth distinct element
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            key=nums[i]
            j=i-1
            while j>=0 and key < nums[j]:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums[-k]
