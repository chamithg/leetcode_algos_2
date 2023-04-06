class Solution:
    def lengthOfLIS(self, nums):
        if not nums: return 0
        N = len(nums)
        dp = [1] * N
        count = [1] * N
        for i in range(N):
            for j in range(i):
                if nums [i] > nums [j]: 
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        count [i] = count [i]
                    elif dp[i]+1 == dp[i]:
                        count [i] += count [j]
        longest_len = max(dp)
        return sum([count[i] for i in range(N) if dp [i]==longest_len])
nums = [1,3,5,4,7]
obj = Solution()
print(obj.lengthOfLIS(nums))