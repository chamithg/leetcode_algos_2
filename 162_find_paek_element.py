class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0

        while i <= len(nums)-1:
            if i == len(nums)-1 or nums[i-1]< nums[i] > nums[i+1]:
                return i
            i+=1