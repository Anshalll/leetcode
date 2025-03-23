class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        results = []
       
        def backtrack(idex, temp  , remaining  ):
            
            currindex = 0
            if remaining == 0:
                 results.append(temp[:])
                 return
            if remaining < 0:
                 return
            for i in range(idex, len(candidates)):
                    
                    currindex = i + 1
                    if i > idex and  candidates[i] == candidates[i - 1]:
                        continue
                    temp.append(candidates[i])

                    backtrack(currindex , temp , remaining - candidates[i]  )
                    temp.pop()             

        backtrack(0 , [] , target)
        return results
        

mysolution = Solution()
print(mysolution.combinationSum2([2,5,2,1,2] , 5))
print(mysolution.combinationSum2([10,1,2,7,6,1,5], 8))