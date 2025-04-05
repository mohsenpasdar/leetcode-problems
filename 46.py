class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(current_idx):
            if current_idx == len(nums):
                res.append(nums[:])
                return
            
            for i in range(current_idx, len(nums)):
                nums[current_idx], nums[i] = nums[i], nums[current_idx]
                backtrack(current_idx + 1)
                nums[current_idx], nums[i] = nums[i], nums[current_idx]
                
        backtrack(0)
        return res
    
solution = Solution()
print(solution.permute([1,2,3]))