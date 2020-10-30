class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        length = len(digits)
        combinations = set()

        def combination(idx, letters):
            if idx == length:
                combinations.add(letters)
            else:
                for letter in digit_to_letters[digits[idx]]:
                    combination(idx + 1, letters + letter)

        combination(0, "")
        combinations.discard("")

        return list(combinations)
