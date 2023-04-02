class Solution:
    def wordBreak(self, s, wordDict):
        run = True
        temps = s[:]
        while temps and run:
            found = False
            for i in range(len(temps)):
                if temps[0:i+1] in wordDict:
                    found = True
                    temps = temps[i+1:]
                    break
            if not found:
                run = False    
        if temps:
            temps2 = s[:]
            run = True
            while temps2 and run:
                found = False
                for i in reversed(range(len(temps2))):
                    if temps2[i:] in wordDict:
                        found = True
                        temps2 = temps2[0:i]
                        break
                if not found:
                    run = False
            if temps2:
                print(temps2)
                return False
            else:
                return True 
        else:
            return True   
        
        


s = "leetcode"
wordDict = ["leet","code"]
obj = Solution()
print(obj.wordBreak(s,wordDict))