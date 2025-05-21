from typing import List


class Solution2:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        output = []
        length = len(heights)
        
        for i in range(length):
            maximum = 0
            count = 0
            
            for j in range(i + 1, length):
                minimum = min(heights[i], heights[j])
                if maximum < minimum:
                    count += 1
                print(i, j)
                
                maximum = max(minimum, maximum)
                if maximum == heights[i]:
                    break
                
            output.append(count)
            
        return output

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        length = len(heights)
        res = [0] * length
        stack = []
        maximum = 0

        for i in reversed(range(length)):
            if heights[i] > maximum:
                res[i] = len(stack)
                stack = [heights[i]]
                maximum = heights[i]
            else:
                count = 1
                while heights[i] > stack[-1]:
                    stack.pop()
                    count += 1
                res[i] = count
                stack.append(heights[i])
                
        return res
    
solution = Solution()
print(solution.canSeePersonsCount([5,11,2,8,10]))
    