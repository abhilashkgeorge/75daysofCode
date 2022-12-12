# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) t
# ime and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from turtle import right
from typing import List


nums = [1,2,3,4]


class Solution(object):



    def product_of_array_except_self(self,nums: List[int]):

        #Note: using the division operator ,Which was clearly not allowed from the question.
        # answers: int = 1
        # for value in nums:
        #     answers = value * answers
        # answer:List[int] = []
        # for i,j in enumerate(nums):
        #     answer.insert(i,int(answers/nums[i]))

        #     print(answer)
        left_prod = []
        right_prod = []
        left_prod.insert(0,1)
        right_prod.insert(len(nums)-1,1)

        for i in range(1,len(nums)):
            left_prod.insert(i,(nums[i-1]*left_prod[i-1]))
        for j in reversed(nums):
            print(j)
            right_prod.insert(j,(nums[j]))
        print(left_prod,right_prod)




obj1 = Solution()
obj1.product_of_array_except_self(nums)