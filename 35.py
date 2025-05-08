from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else: 
                start = mid + 1
        
        if target <= nums[start]:
            return start
        else:
            return start + 1
        
        
                   
solution = Solution()
print(solution.searchInsert([1,3,5,6, 7], 8))

# a = [1, 2, 3]
# print(55//10)



class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while end - start > 1:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid
            else:
                end = mid
            
        if target <= nums[start]:
            return start
        elif target > nums[end]:
            return end + 1
        else: return end