class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            else: # ), ], }
                try:
                    if stack.pop() != bracketMap[b]:
                        return False
                except IndexError as ie: # handles popping an empty stack list
                    return False
        
        if not stack:
            return True
        else:
            return False