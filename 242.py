class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        for char in t:
            if s_map.get(char, 0) == 0:
                return False
            s_map[char] -= 1
        
        return True
solution = Solution()
print(solution.isAnagram("anagram", ("nagaram")))
# print('mohsen'[-6])
            