import numpy
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        output =[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if numpy.prod(nums[i:j+1]) < k:
                    output.append(nums[i:j+1])
        return len(output)
