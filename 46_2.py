class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        
        def helper(temp, nums):
            if len(nums) == 0:
                res.append(temp[:])
                return
            
            for i in range(len(nums)):
                new_temp = temp + [nums[i]]
                new_nums = nums[:i] + nums[i + 1:]
                helper(new_temp, new_nums)
            
        helper(temp, nums)
        return res
    
solution = Solution()
print(solution.permute([1,2,3]))