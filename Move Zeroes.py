# Move Zeroes
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.Note that you must do this in-place without making a copy of the array.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # l=[]
        # m=[]
        # for i in nums:
        #     if i!=0:
        #         m.append(i)
                
        #     else:
        #         l.append(i)
        # print(sorted(m)+l)
        non_zero_elements = [i for i in nums if i != 0]
        zero_elements = [i for i in nums if i == 0]
        nums[:] = non_zero_elements + zero_elements
