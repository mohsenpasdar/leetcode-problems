from typing import List


class Solution2:
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
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        
        output[0] = nums[0]
        for i in range(1, n):
            output[i] = nums[i] * output[i - 1]
        
        mult = 1
        for j in range(n - 1, 0, -1):
            output[j] = output[j - 1] * mult
            mult *= nums[j]
        
        output[0]  = mult
    
        return output
            
solution = Solution()
print(solution.productExceptSelf([-1,1,5,-3,2]))