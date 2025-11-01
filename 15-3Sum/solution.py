class Solution:
    def compareLists(self, list1: List[int], list2: List[int]) -> bool:
        # assumes the lists are already sorted
        #if len(list1) != len(list2):
        #    raise "COMPARE LIST ERROR"
        
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True # all values are equal

    def twoSum(self, nums: dict, initial: int) -> List[int]:
        seen = nums.copy()
        target = 0 - initial
        
        seen[initial] -= 1 # ensure we remove this copy

        results = []
        for key, value in seen.items():
            if value > 0:
                complement = target - key
                seen[key] -= 1

                if complement in seen and seen[complement] > 0:
                    seen[complement] -= 1
                    results.append([initial, key, complement])

        return results
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we don't want to take away globally
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1

        solutions = []
        solutionTuples = {}
        for key in numDict.keys():
            results = self.twoSum(numDict, key)
            #print("RESULTS", results)
            if results:
                #result.sort()
                for result in results:
                    result.sort()
                    
                    t = tuple(result)
                    if t not in solutionTuples:
                        solutions.append(result)
                        solutionTuples[t] = 0
                    


        #print(solutions)
        return solutions
