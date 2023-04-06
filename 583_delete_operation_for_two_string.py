class Solution:
    def minDistance(self, word1, word2):
        
        #  to solve this problem, we should find the longest common subsequence and get the sum of excess length of 
        #  each word as delete steps
        len1 = len(word1)
        len2 = len(word2)
        
        table =[[0 for col in range(len1+1)] for row in range(len2+1)]

        for r in range(1,len2+1):
            for c in range(1,len1+1):
                if word2[r-1] == word1[c-1]:
                    table[r][c] = table[r-1][c-1]+1
                else:
                    table[r][c] = max(table[r][c-1],table[r-1][c])

        lontest_commen_seq = table[-1][-1]
        
        return (len1-lontest_commen_seq)+(len2-lontest_commen_seq)
        
        
        

word1 = "sea"
word2 = "eat"
obj = Solution()
print(obj.minDistance(word1,word2))
