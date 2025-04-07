class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1, n + 1)]
        
        def helper(reminder):
            if reminder == 1: 
                return ''.join(str(num) for num in nums)
            
            factorial = 1
            multi = 1
            while reminder > factorial:
                multi += 1
                factorial *= multi
            factorial //= multi
            multi -= 1
            curr_index = len(nums) - multi - 1
            q = reminder // factorial
            new_reminder = reminder % factorial
            if new_reminder == 0:
                q -= 1
                new_reminder = factorial
            temp = curr_index + 1
            while q > 0:
                nums[curr_index], nums[temp] = nums[temp], nums[curr_index]
                temp += 1
                q -= 1
            print(new_reminder)
            return helper(new_reminder)        
        return helper(k)
    
print(Solution().getPermutation(9, 360))