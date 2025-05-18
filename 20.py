class Solution2:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 == 1: return False
        
        match = {"()", "[]", "{}"}
        
        def helper(i, j):
            if i >= length - 1 or j >= length:
                return False
        
            if s[i] + s[j] in match:
                return j + 1
            
            if s[i] in "([{" and s[j] in "([{":
                temp = helper(j, j + 1)
                if temp:
                    return helper(i, temp)
            
            return False
            
        idx = 0
        while idx < length:
            temp_idx = helper(idx, idx + 1)
            
            if not temp_idx: return False
            
            idx = temp_idx
        
        return True
  

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"()", "[]", "{}"}
        
        for c in s:
            if not stack:
                if c in ")]}": return False
                stack.append(c) 
            elif stack[-1] + c in match:
                stack.pop()
            elif c in ")}]":
                return False
            else: stack.append(c)
        
        return not stack
        
solution = Solution()
print(solution.isValid("[[[]]]"))
