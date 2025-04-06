class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(curr_idx, my_set):
            if curr_idx == len(nums):
                res.append(nums[:])
                return
            
            for i in range(curr_idx, len(nums)):
                if nums[i] in my_set:
                    continue
                nums[curr_idx], nums[i] = nums[i], nums[curr_idx]
                backtrack(curr_idx + 1, set())
                nums[curr_idx], nums[i] = nums[i], nums[curr_idx]
                my_set.add(nums[i])
                
        backtrack(0, set())
        return res

solution = Solution()
print(solution.permuteUnique([1,2,1]))