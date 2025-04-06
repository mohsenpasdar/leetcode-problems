class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        found = False
        left, right = 0, length - 1
        for i in reversed(range(1, length)):
            if nums[i - 1] < nums [i]:
                for j in range(i, length):
                    if nums[i - 1] >= nums[j]:
                        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
                        found = True
                        break
                    if j == length - 1:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        found = True
                    
                left, right = i, length - 1
                if found:
                    break
                
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return 
                    
arr = [9, 1, 7, 6, 3]           
Solution().nextPermutation(arr)
print(arr)
# for i in reversed(range(3, 5)):
#     print(i)
# # A = [1, 2, 3]
# print(A[-1])
    