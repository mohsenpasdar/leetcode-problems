from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used_third = set()
        result = []

        def two_sum(start: int, target: int) -> List[List[int]]:
            explored = set()
            used_in_pair = set()
            pairs = []

            for idx in range(start, n):
                x = nums[idx]
                if x in used_in_pair or x in used_third:
                    continue

                need = target - x
                if need in explored:
                    pairs.append([need, x])
                    used_in_pair.add(x)
                    used_in_pair.add(need)
                else:
                    explored.add(x)

            return pairs

        for i in range(n - 2):
            third = nums[i]
            if third in used_third:
                continue

            pairs = two_sum(i + 1, -third)
            if pairs:
                used_third.add(third)
                for a, b in pairs:
                    triplet = [a, b, third]
                    result.append(triplet)
        return result

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def twosum(i, target):
            found = set()
            explored = set()
            twoSumOutput = []
            for idx in range(i, n): 
                if nums[idx] in found or nums[idx] in uniquethird:
                    continue              
                if (target - nums[idx]) in explored:
                    twoSumOutput.append([target - nums[idx], nums[idx]])
                    found.add(nums[idx])
                    found.add(target - nums[idx])
                else:
                    explored.add(nums[idx])
                    
            return twoSumOutput
        
        result = []
        uniquethird = set()
        for i in range (n - 2):
            if nums[i] in uniquethird:
                continue
                
            currentTwoSum = twosum(i + 1, -1 * nums[i])
            if currentTwoSum:
                uniquethird.add(nums[i])
                for j in currentTwoSum:
                    s = j + [nums[i]]
                    result.append(s)
                
        return result
        
        
        
solution = Solution()
print(solution.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
