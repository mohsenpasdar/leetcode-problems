from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        
        while min_speed < max_speed:
            speed = (min_speed + max_speed) // 2
            time = 0
            
            for bananas in piles:
                time += ceil(bananas / speed)
            
            if time > h:
                min_speed = speed + 1
            else:
                max_speed = speed
        
        return max_speed 
            


solution = Solution()
print(solution.minEatingSpeed([30,10,20], 6))