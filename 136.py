from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        
        for num in nums:
           temp = temp ^ num 
           
        return temp

solution = Solution()
print(solution.singleNumber([4,1,2,1,2]))