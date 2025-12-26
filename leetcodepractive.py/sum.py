class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# Test
s = Solution()
print(s.twoSum([2,7,11,15], 9))  
print(s.twoSum([3,2,4], 6))      
print(s.twoSum([3,3], 6))        