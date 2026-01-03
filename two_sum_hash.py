# Two Sum – LeetCode

Problem: Find indices of two numbers that add up to target.

Approach:
- Used Hash Table (dictionary)
- Time Complexity: O(n)
- Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            needed=target-nums[i]
            if needed in seen:
                return[seen[needed],i]
            seen[nums[i]]=i

nums=[2,7,11,15]
target=9
solution=Solution()
result=solution.twoSum(nums,target)

print(result)  
