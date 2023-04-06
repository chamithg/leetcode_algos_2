class Solution:
    def integerBreak(self, n: int) -> int:
        self.maxProd = 0

        visited = set()

        def findMax (number,path,product):
            if number == 0:
                if sum(path) == n and len(path) > 1: self.maxProd = max(self.maxProd,product)
                return
            else:
                for i in range(1,number+1):
                    if (number-i,product *i) not in visited:
                        visited.add((number-i,product *i))
                        temp_path = path[:]
                        temp_path.append(i)
                        findMax(number-i,temp_path,product * i)
        
        findMax(n,[],1)

        return self.maxProd

