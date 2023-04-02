class Solution:
    def wordBreak(self, s, wordDict):
        D = set(wordDict)
        N = len(s)
        dp = [False] * (N+1)
        dp[0] = True
        
        for start in range(N):
            if not dp[start]: continue
            for end in range(start+1,N+1):
                if s[start:end] in wordDict:
                    dp[end] = True
        
        return dp[-1]
        
        


s = "leetcode"
wordDict = ["leet","code"]
obj = Solution()
print(obj.wordBreak(s,wordDict))