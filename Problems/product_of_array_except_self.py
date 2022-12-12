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

# This is complex why do it this way I have no clue yet but seems reasonable but chatGPT explained the solution way better to me than these youtube channel solution 
# I really need to learn to solve all these problems myself , planning on starting a startup fed up of sitting still in a company I want to use my resources to its full potential.

        # left_prod = []
        # right_prod = []
        # left_prod.insert(0,1)
        # right_prod.insert(len(nums)-1,1)

        # for i in range(1,len(nums)):
        #     left_prod.insert(i,(nums[i-1]*left_prod[i-1]))
        # for j in reversed(nums):
        #     print(j)
        #     right_prod.insert(j,(nums[j]))
        # print(left_prod,right_prod)


# THE ULTIMATE SOLUTION

        # # Create a new array to store the result
        # result = []
        
        # # Loop through the input array
        # for i in range(len(nums)):
        #     # Initialize a variable to store the product
        #     # Set it to 1 initially to account for the fact
        #     # that we will be multiplying the elements together
        #     product = 1
            
        #     # Loop through the array again, excluding the current element
        #     for j in range(len(nums)):
        #         if i != j:
        #             # Multiply the current element with the product
        #             product *= nums[j]
            
        #     # Append the product to the result array
        #     result.append(product)
        
        # # Return the result array
        # return result

#Time limit exceed for the above one  so the next attempt

        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


obj1 = Solution()
obj1.product_of_array_except_self(nums)