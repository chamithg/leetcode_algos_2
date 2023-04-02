class Solution:
    def lengthOfLIS(self, nums):
        N = len(nums)
        dp = [1]* N

        for i in range(N):
            for j in range(i):
                if nums[i]> nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
                

        print(dp)
        return max(dp)
nums = [10,9,2,5,3,7,101,18]
obj = Solution()
print(obj.lengthOfLIS(nums))