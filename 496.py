from typing import List


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        nums2_dic = {}
        length = len(nums2)
        for idx, num in enumerate(nums2):
            nums2_dic[num] = idx
            
        for i, elem in enumerate(nums1):
            for j in range(nums2_dic[elem], length):
                if nums2[j] > elem:
                    ans[i] = nums2[j]
                    break
                    
        return ans

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack = []        
        index_map = { num: idx for idx, num in enumerate(nums1)}
            
        for num in reversed(nums2):
            while stack and num > stack[-1]:
                stack.pop()
            
            if num in index_map:
                ans[index_map[num]] = stack[-1] if stack else -1
            
            stack.append(num)
                   
        return ans
    
solution = Solution()
print(solution.nextGreaterElement([4,1,2], [1,3,4,2]))