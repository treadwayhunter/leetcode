class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = 101
        nums.sort()
        count = 0
        for num in nums:
            if num != 101:
                count += 1
            else: 
                break

        return count