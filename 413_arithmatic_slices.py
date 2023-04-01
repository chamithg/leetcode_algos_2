class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        def countOfSlices(len_num):
            output = 0
            if len_num < 3:
                return output
            else:
                output +=1
                len_num -=3
                n = 2
                while len_num > 0:
                    output += n
                    n+=1
                    len_num -=1
            return output

        conseq_count = 0
        diff = nums[1] - nums[0]
        for i in range(len(nums)-1):
            if nums[i+1]- nums[i] == diff:
                conseq_count +=1
                if i == len(nums)-2:
                    conseq_count+=1
                    if conseq_count >= 3:
                        count += countOfSlices(conseq_count)
                    
            else:
                conseq_count +=1
                if conseq_count >= 3:
                    count += countOfSlices(conseq_count)
                conseq_count = 1
                diff = nums[i+1]- nums[i]
        
        return count

nums = [1,2,3,4,6]
obj = Solution()
print(obj.numberOfArithmeticSlices(nums))