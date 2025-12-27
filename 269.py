from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        all_chars = set()
        for word in words:
            for char in word:
                all_chars.add(char)
        
        adj = {char: set() for char in all_chars}
        state = {char: 0 for char in all_chars}
        output = []
        
        for i in range(len(words) - 1):         
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            j = 0
            while j < min_len and w1[j] == w2[j]:
                j += 1

            # prefix invalid case: "abc" before "ab"
            if j == min_len and len(w1) > len(w2):
                return ""

            # found first different character
            if j < min_len:
                adj[w1[j]].add(w2[j])
        
        def dfs_cycle(char):
            state[char] = 1
            for c in adj[char]:
                if state[c] == 1:
                    return True
                if state[c] == 0 and dfs_cycle(c):
                    return True
            
            state[char] = 2
            output.append(char)
            return False
            
        for c in adj.keys():
            if (state[c] == 0) and dfs_cycle(c):
                return ''
            
        output.reverse()

        return ''.join(output)
    
solution = Solution()
print(solution.foreignDictionary(["art", "arsn"]))


