class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # res = []
        # nums = [i for i in range(1, n + 1)]
                
        # def helper(permutation, remainingNums):
        #     if len(remainingNums) == 0:
        #         res.append(permutation[:])
        #         return
                
        #     for i in range(len(remainingNums)):
                
        #         newPermutation = permutation + [remainingNums[i]]
        #         newRemainingNums = remainingNums[:i] + remainingNums[i + 1:]
        #         helper(newPermutation, newRemainingNums)
        
        # helper([], nums)
        # return ''.join(str(num) for num in res[k - 1])
        
        nums = [i for i in range(1, n + 1)]
    
                
        def helper(permutation, remainingNums, k, current):
            if len(remainingNums) == 0:
                return (current + 1, permutation)
                
            for i in range(len(remainingNums)):
                
                newPermutation = permutation + [remainingNums[i]]
                newRemainingNums = remainingNums[:i] + remainingNums[i + 1:]
                (current, newPermutation) = helper(newPermutation, newRemainingNums, k, current)
                if current == k:
                    return (current, newPermutation)
            return (current, newPermutation)
        
        (current, newPermutation) = helper([], nums, k, 0)
        return ''.join(str(num) for num in newPermutation)           


solution = Solution()
print(solution.getPermutation(9, 480))