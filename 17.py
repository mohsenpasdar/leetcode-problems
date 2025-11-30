class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        digits_dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        output = []
        def helper(permutation, digits):
            if len(digits) == 0:
                output.append(permutation)
                return
            
            for char in digits_dic[digits[0]]:
                helper(permutation + char, digits[1:])
            
        helper('', digits)
        return output
        
solution = Solution()
print(solution.letterCombinations(""))

# a = 's'
# print(a[0:]) / test