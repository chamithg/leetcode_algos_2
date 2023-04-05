class Solution:

    # dynamic programming solution
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        
        table =[[0 for col in range(len1+1)] for row in range(len2+1)]

        for r in range(1,len2+1):
            for c in range(1,len1+1):
                if text2[r-1] == text1[c-1]:
                    table[r][c] = table[r-1][c-1]+1
                else:
                    table[r][c] = max(table[r][c-1],table[r-1][c])

        return table[-1][-1]
        

text1 = "bsbininm"
text2 = "jmjkbkjkv"
obj = Solution()

print(obj.longestCommonSubsequence(text1,text2))


[[0, 1, 1, 2, 2, 2, 2, 2, 2], 
 [0, 1, 1, 2, 2, 2, 2, 2, 2], 
 [0, 1, 1, 2, 2, 2, 2, 2, 2],
 [0, 1, 1, 2, 2, 2, 2, 2, 2], 
 [0, 1, 1, 2, 2, 2, 2, 2, 2], 
 [0, 1, 1, 2, 2, 2, 2, 2, 2], 
 [0, 1, 1, 2, 2, 2, 2, 2, 2], 
 [0, 1, 1, 2, 2, 2, 2, 2, 2], 
 [0, 1, 1, 2, 2, 2, 2, 2, 2], 
 [0, 1, 1, 2, 2, 2, 2, 2, 2]]