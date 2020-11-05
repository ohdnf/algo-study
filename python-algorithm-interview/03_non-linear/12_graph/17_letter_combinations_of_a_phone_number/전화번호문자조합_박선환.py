class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_chr = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        
        digits = list(digits)
        result = []
        def dfs(cnt, output):
            if cnt == len(digits):
                if output:
                    result.append(output)
                return
            for chr in num_chr[digits[cnt]]:
                dfs(cnt + 1, output + chr)
        dfs(0, '')
        return result