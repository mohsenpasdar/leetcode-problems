class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        
        def helper(subset, nums):
            if len(nums) == 0:
                return 
            
            for i, num in enumerate(nums):
                newSubset = subset + [num]
                output.append(newSubset[:])
                helper(newSubset, nums[i + 1:])
        
        helper([], nums)
        
        return output
        
        
solution = Solution()
print(solution.subsets([1,2,3]))

# a = [1, 2, 3]
# print(a[3:])