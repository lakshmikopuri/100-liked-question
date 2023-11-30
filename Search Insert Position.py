#Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag=0
        for i in range(len(nums)):
            if target==nums[i]:
                return i
                flag=1
            else:
                flag=0
        if flag==0:
            nums.append(target)
        nums.sort()
        for i in range( len(nums)):
            if nums[i]==target:
                return i
        print(nums)
        return nums[0]
