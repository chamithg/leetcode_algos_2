class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        right = 1
        len_num = len(nums)
        if len_num < 2:
            if nums[0]>= target:
                return 1
            else:
                return 0
        min_len = 999999
        temp_sum = nums[left] + nums[right]
        
        while right <= len_num:
            if nums[left] >= target:
                return 1
            if left < right:
                if temp_sum < target:
                    right +=1
                    if right< len_num:
                        temp_sum += nums[right]
                else:
                    min_len = min(min_len,len(nums[left:right+1]))
                    temp_sum -= nums[left]
                    left +=1
            else:
                right +=1
                if right< len_num:
                    temp_sum += nums[right]
        if min_len == 999999:
            return 0   
        return min_len  
        
target = 7
nums = [2,3,1,2,4,3]
obj = Solution()

print(obj.minSubArrayLen(target,nums))