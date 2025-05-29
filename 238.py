from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        
        zero_count  = 0
        total_product = 1
        zero_index = -1
        
        for i, num in enumerate(nums):           
            if num == 0: 
                zero_count  += 1
                if zero_count > 1: return output
                zero_index = i
            else:
                total_product *= num
        
        if zero_count  == 1:
            output[zero_index] = total_product
            return output
        
        for i in range(n):
            output[i] = total_product // nums[i]
        
        return output
    
solution = Solution()
print(solution.productExceptSelf([-1,1,5,-3,2]))