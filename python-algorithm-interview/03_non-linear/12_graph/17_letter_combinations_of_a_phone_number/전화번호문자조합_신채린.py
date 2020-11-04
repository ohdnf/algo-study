class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(letter, depth):
            if depth >= len(digits):
                result.append(letter)
                letter = ""
                return
            for each in numbers[int(digits[depth])]:
                dfs(letter + each, depth + 1)
        
        numbers = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'],
                   ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                   ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']
                  ]
        result = []
        for letter in numbers[int(digits[0])]:
            dfs(letter, 1)
        return result