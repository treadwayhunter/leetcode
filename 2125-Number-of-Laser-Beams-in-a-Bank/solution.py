class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
 
        beamCounter = 0
        currentRowCount = 0 # current Row
        lastRowCount = 0 # the last row containing devices
        
        for row in bank:
            # multiply count of 1s in current row times number in the next row
            currentRowCount = row.count("1")
            #if currentRowCount > 0:
            #    beamCounter += (lastRowCount * currentRowCount)
            #    lastRowCount = currentRowCount
            if currentRowCount == 0:
                continue
            beamCounter += (lastRowCount * currentRowCount)
            lastRowCount = currentRowCount

        return beamCounter