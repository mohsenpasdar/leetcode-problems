from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def helper(n):
            if n == 0:
                return 1
            if n < 0:
                return 1 / self.myPow(x, -n)
            if n == 1:
                return x
            
            if n in memo.keys():
                return memo[n]
            else:
                memo[n] = helper(n // 2) * helper(n - n // 2)
                return memo[n]
    
        return helper(n)
solution = Solution()

class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        half = self.myPow(x, n // 2)
        return half * half if n % 2 == 0 else half * half * x

class Solution3:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        
        base = x
        result = 1
        
        while n > 0:
            if n % 2 == 1:
                result *= base
            base = base * base
            n = n // 2
        return result
    
solution = Solution2()
# print(solution.myPow(2.10000, 3))
print(solution.myPow(2, 32))

