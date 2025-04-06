class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(permutation, remaining, my_set):
            if len(remaining) == 0:
                res.append(permutation[:])
                return
            
            for i in range(len(remaining)):
                if remaining[i] in my_set:
                    continue
                my_set.add(remaining[i])
                new_permutation = permutation + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(new_permutation, new_remaining, set())
                                 
        backtrack([], nums, set())
        return res    
        

solution = Solution()
print(solution.permuteUnique([1,2,1]))