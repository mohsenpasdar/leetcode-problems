from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        def helper(s1: str, s2: str):
            if len(s1) != len(s2): return False
            
            char_count = {}
            
            for char in s1:
                char_count[char] = char_count.get(char, 0) + 1
                
            for char in s2:
                if char_count.get(char, 0) == 0:
                    return False
                char_count[char] -= 1
            
            return True
        
        for current_str in strs:
            matched  = False
            for key_str in anagram_groups.keys():
                if helper(current_str, key_str):
                    anagram_groups[key_str].append(current_str)
                    matched  = True
                    break
            if not matched :
                anagram_groups[current_str] = [current_str]

        return list(anagram_groups.values())
    
solution = Solution()
# print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(''.join(sorted("mohsen")))