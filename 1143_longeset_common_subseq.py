class Solution:
    
    
    #  top down recursive method
    # exponential time complexity
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.maxlen = 0
        
        def find(t1,t2,temp_len):
            if t1 == len(text1) or t2 == len(text2):
                return 
            elif text1[t1] == text2[t2]:
                self.maxlen = max(self.maxlen,temp_len+1)
                find(t1+1,t2+1,temp_len+1)
            else:
                find(t1,t2+1,temp_len)
                find(t1+1,t2,temp_len)
        
        find(0,0,0)
        return self.maxlen
        
        
        
        
        
        

text1 = "abcde"
text2 = "ace"
obj = Solution()

print(obj.longestCommonSubsequence(text1,text2))