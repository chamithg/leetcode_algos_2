class Solution:
    def intervalIntersection(self, firstList, secondList) :
        comb = sorted(firstList + secondList)

        output = []
        found_max = float(-999999990)
        for i in range(len(comb)-1):
            found_max = max(found_max,comb[i][1])
            start = comb[i][0]
            end = comb[i][1]
            
            if comb[i+1][0] < end:
                start = max(start,comb[i+1][0])
                end = min(end,comb[i+1][1])
                output.append([start,end])
            if comb[i][1] == comb[i+1][0]:
                output.append([comb[i][1],comb[i][1]])
        
        if comb[-1][0]> output[-1][1] and comb[-1][0] < found_max:
            output.append([comb[-1][0],min(comb[-1][1],found_max)])
            
        print(comb)    
        return output
            
            

firstList = [[3,5],[9,20]]
secondList = [[4,5],[7,10],[11,12],[14,15],[16,20]]

# conb = [[3, 5], [4, 5], [7, 10], [9, 20], [11, 12], [14, 15], [16, 20]]
# Output: [[4,5],[9,10],[11,12],[14,15],[16,20]]

obj = Solution()
print(obj.intervalIntersection(firstList,secondList))