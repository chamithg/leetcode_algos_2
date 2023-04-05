class Solution:
    def findNumberOfLIS(self, nums):
        
        N  = len(nums)
        count = 0
        dp = [1]* N
        # first find the longest increasing subsequence length
        for i in range(N):
            for j in range(i):
                if nums[i]> nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        max_len = max(dp)
        
        def find_max (arr,i):
            if i>=N:
                return
            if len(arr) == max_len:
                count +=1
                return
            if nums[i]> arr[-1]:
                temp_arr = arr[:]
                temp_arr.append(nums[i])
                find_max(temp_arr,i+1)
            else:
                find_max(arr,i+1)
                
        find_max([nums[0]],1)
        return count
nums = [1,3,5,4,7]
obj = Solution()
print(obj.findNumberOfLIS(nums))

        