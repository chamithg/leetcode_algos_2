class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1 and  nums[i] > nums[i-1] :
            i+=1
        if i == len(nums)-1:
            if nums[0]< nums[i]:
                return nums[0]
            else:
                return nums[i]
        else:
            return nums[i]