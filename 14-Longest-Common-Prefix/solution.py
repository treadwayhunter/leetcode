class Solution:
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ###################################
        # If all strings are empty, just return ""
        checkEmpty = True
        for s in strs:
            if s:
                checkEmpty = False
                break
        
        if checkEmpty:
            return ""
        ###################################
        ###################################
        # Determine shortest string in the list
        shortestLen = 201 # set to 201, as longest string is 200
        for s in strs:
            if len(s) < shortestLen:
                shortestLen = len(s)
        ###################################
        ###################################
        # check for longest shared prefix
        lastPrefix = ""
        for i in range(0, shortestLen + 1):
            prefix = strs[0][0:i]

            for s in strs:
                if not s.startswith(prefix):
                    return lastPrefix
            
            lastPrefix = prefix
        return lastPrefix