# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order

class Solution():
    nums = [3,2,4]  
    target = 6      

    def two_sums(self,number, result):
        i = 0
        j= 1
        for i in range(len(number)):     #len(element) is used to get the length
            for j in range(j,len(number)):     #count(element) is used to get the occurence of the same element
                if self.target == number[i] + number[j]:
                    print("Answer found {} ".format([i,j]))  # can use + or  value inside {element}
                j = j+1
            i = i+1
            j = i + 1

obj1 = Solution()
obj1.two_sums(obj1.nums, obj1.target)



