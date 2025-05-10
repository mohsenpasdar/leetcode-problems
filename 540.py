from typing import List

# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         length = len(nums)
        
#         for idx in range(0, length - 1, 2):
#             if nums[idx] != nums[idx + 1]:
#                 return nums[idx]
            
#         return nums[-1]
                   
# solution = Solution()
# print(solution.singleNonDuplicate([1]))

# a = [1, 2, 3]
# print(55//10)

class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if (mid - left) % 2 != 0:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    right = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    right = mid
                elif nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    return nums[mid]
        
        return nums[left] 
        
solution = Solution2()
print(solution.singleNonDuplicate([1]))