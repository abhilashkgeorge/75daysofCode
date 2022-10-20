# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash = set()
#         for value in nums:
#             if value in hash:
#                 return True
#             else:
#                 hash.add(value)
#         return False
       
        

from traceback import print_tb
from typing import List, Set


numbers = [1,2,3,4]

class Solution:
    def contains_duplicates(self,nums: List[int])->bool:
        hash = set()
        for value in nums:
            if value in hash:
                return True
            else:
                hash.add(value)
        return False

        # new_set = set(nums)
        # if len(nums)==len(new_set):
        #     print("True")
        # print(new_set)
        # i=0
        # j=1
        # for i_index in range(i,len(nums)-1):
        #     for j_index in range(j,len(nums)):
        #         if(nums[i]==nums[j]):
        #             print("true")
        #             return
        #         j+=1
            
        #     i+=1
        #     j=i+1
        # print("False")
            


obj = Solution()
print(obj.contains_duplicates(numbers))