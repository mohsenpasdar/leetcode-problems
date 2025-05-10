from typing import List

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8 * n) ** 0.5)) // 2

class Solution2:
    def arrangeCoins(self, n: int) -> int:
        rows = 1
        sum = 1
        
        while sum <= n:
            rows += 1
            sum += rows
            
        
        return rows - 1

class Solution3:
    def arrangeCoins(self, n: int) -> int:
        left, right = int(n ** 0.5), 2 * int(n ** 0.5)
        
        while left <= right:
            mid = (left + right) // 2
            num = mid * (mid + 1) / 2
            
            if num == n: return mid
            
            if num > n:
                right = mid - 1
            else:
                left = mid + 1
        
        return right
        
solution = Solution3()
print(solution.arrangeCoins(56))