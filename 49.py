from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for current_str in strs:
            sorted_str = ''.join(sorted(current_str))
            anagram_groups[sorted_str] = anagram_groups.get(sorted_str, []) + [current_str]

        return list(anagram_groups.values())
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for current_str in strs:
            current_str_list = [0] * 26
            for char in current_str:
                current_str_list[ord(char) - 97] += 1
            
            current_str_tuple = tuple(current_str_list)

            if current_str_tuple in anagram_groups:
                anagram_groups[current_str_tuple].append(current_str)
            else:
                anagram_groups[current_str_tuple] = [current_str]

        return list(anagram_groups.values())
solution = Solution()

print(solution.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))
# print(''.join(sorted("mohsen")))

