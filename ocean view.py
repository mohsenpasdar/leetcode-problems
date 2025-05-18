class Solution2:
    def ocean_view_list(self, buildings: list) -> list:
        stack = []
        
        for building, height in enumerate(buildings):
            if stack:
                while stack and height >= buildings[stack[-1]]:
                    stack.pop()
                    
            stack.append(building)
        
        return stack

class Solution:
    def ocean_view_list(self, buildings: list) -> list:
        res = []
        max = 0
        length = len(buildings)
        
        for idx in reversed(range(length)):
            if buildings[idx] > max:
                res.append(idx)
                max = buildings[idx]
        
        return res[::-1]
            
solution = Solution()
print(solution.ocean_view_list([2,2,2,2]))

