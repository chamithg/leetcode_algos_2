class Solution:
    def numDecodings(self, s):
        if s[0]== "0" or not s: return 0
        N = len(s)
        if N == 1:return 1
        dp = [0]* N 
        dp[0] = 1
        if s[1] =="0":    
            if s[0]=="1" or s[0]=="2":
                dp[1]=1
            else:
                return 0  
        else:
            if 10<=int(s[0:2])<=26:
                dp[1]=2
            else:
                dp[1]=1
        for i in range(2,N):
            if s[i] !="0":    
                if 10<=int(s[i-1:i+1])<=26:
                    dp[i]=dp[i-1]+dp[i-2]
                else:
                    dp[i]=dp[i-1]    
            else:
                if 10<=int(s[i-1:i+1])<=26:
                    dp [i]=dp[i-2]
                else:
                    return 0
        print(dp)
        return dp[-1]

s ="1244532324523212312231231"

obj = Solution()
print(obj.numDecodings(s))