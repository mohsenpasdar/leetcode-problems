class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1, n + 1)]
        
        while k > 1:
            factorial = 1
            multi = 1
            while k > factorial:
                multi += 1
                factorial *= multi
            factorial //= multi
            multi -= 1
            curr_index = len(nums) - multi - 1
            q, new_k = divmod(k, factorial)

            if new_k == 0:
                q -= 1
                new_k = factorial
            temp = curr_index + 1
            while q > 0:
                nums[curr_index], nums[temp] = nums[temp], nums[curr_index]
                temp += 1
                q -= 1
            k = new_k
        
        return ''.join(str(num) for num in nums)
    
print(Solution().getPermutation(4, 19))