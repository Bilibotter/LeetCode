class Solution:
    def __init__(self):
        self.maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        if len(digits) == 1:
            return list(self.maps[digits])

        preview = self.letterCombinations(digits[:-1])
        behind = self.maps[digits[-1]]

        return [p + b for b in behind for p in preview]
