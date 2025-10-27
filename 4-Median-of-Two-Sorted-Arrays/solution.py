class Solution:
    # tuple (even, len)
    def isEvenAndLength(self, l):
       # return len(l) % 2 == 0 # excruciatingly slow
        length = len(l)
        return (length & 1 != 1, length)

    def mergeLists(self, l1, l2):
        new_l = [*l1, *l2]
        new_l.sort()
        return new_l

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #print(self.mergeLists(nums1, nums2))
        merge_l = self.mergeLists(nums1, nums2)
        isEven, length = self.isEvenAndLength(merge_l)
        #length = len(merge_l) # calculated the list again

        median = 0
        if isEven:
            half = int(length / 2)
            median = (merge_l[half - 1] + merge_l[half]) / 2
        else:
            half = length // 2
            median = merge_l[half]

        return median