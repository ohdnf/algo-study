class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha = dict()
        alpha["2"] = "abc"
        alpha["3"] = "def"
        alpha["4"] = "ghi"
        alpha["5"] = "jkl"
        alpha["6"] = "mno"
        alpha["7"] = "pqrs"
        alpha["8"] = "tuv"
        alpha["9"] = "wxyz"
        

        result = []
        if len(digits) == 0:
            return result
        def dfs(st):
            if len(st) == len(digits):
                result.append(st)
            else:
                for c in alpha[ digits[len(st)] ]:
                    dfs(st+c)
        dfs("")
        return result
# 24 ms	14.1 MB	python3