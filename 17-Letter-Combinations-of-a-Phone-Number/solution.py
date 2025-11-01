class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        buttonMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        output = []

        #s = ""
        #if len(digits) == 1:
        #    for letter in buttonMap[digits[0]]:
        #        output.append(letter)
        #elif len(digits) == 2:
        #    for letter1 in buttonMap[digits[0]]:
        #        for letter2 in buttonMap[digits[1]]:
        #            output.append(letter1 + letter2)
        #elif len(digits) == 3:
        #    for letter1 in buttonMap[digits[0]]:
        #        for letter2 in buttonMap[digits[1]]:
        #            for letter3 in buttonMap[digits[2]]:
        #                output.append(letter1 + letter2 + letter3)
        #elif len(digits) == 4:
        #    for letter1 in buttonMap[digits[0]]:
        #        for letter2 in buttonMap[digits[1]]:
        #            for letter3 in buttonMap[digits[2]]:
        #                for letter4 in buttonMap[digits[3]]:
        #                    output.append(letter1 + letter2 + letter3 + letter4)
        #return output

        def backtrack(index: int, path: str):
            if index == len(digits):
                output.append(path)
                return 

            letters = buttonMap[digits[index]]
            for ch in letters:
                backtrack(index + 1, path + ch)

        backtrack(0, "")
        return output