class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        wordList = [[] for i in range(numRows)]
        currentRow = 0
        goDown = True # true is down, # false is up
        
        for ch in s:
            wordList[currentRow].append(ch)
            
            if goDown:
                currentRow += 1
            else:
                currentRow -= 1

            if currentRow == numRows - 1:
                goDown = False
            elif currentRow == 0:
                goDown = True

        return "".join("".join(row) for row in wordList)