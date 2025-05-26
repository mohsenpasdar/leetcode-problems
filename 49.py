from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for current_str in strs:
            sorted_str = ''.join(sorted(current_str))
            anagram_groups[sorted_str] = anagram_groups.get(sorted_str, []) + [current_str]

        return list(anagram_groups.values())
    
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# print(''.join(sorted("mohsen")))