class Solution:
    def minSubArrayLen(self, target, nums):
        left,temp_sum = 0,nums[0]
        
        if temp_sum >= target:
            return 1

        min_len = float("inf")
        for right in range(1,len(nums)):
            temp_sum += nums[right]
            while temp_sum >= target:
                min_len = min(min_len, right +1 -left)
                temp_sum -= nums[left]
                left+=1

        if min_len == float("inf"):
            return 0
        else:
            return min_len
        
target = 7
nums = [2,3,1,2,4,3]
obj = Solution()

print(obj.minSubArrayLen(target,nums))