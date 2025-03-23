class Solution(object):
    def combinationSum(self, candidates, target):
        results = []    

        

        def backtrack(arrindex , temp , remaining):
            if remaining == 0:
                results.append(temp[:])
                return
            if remaining < 0:
                return
            
            for i in range(arrindex , len(candidates)):
                temp.append(candidates[i])
                backtrack(i , temp , remaining - candidates[i]  )
                temp.pop()

        backtrack(0 , [] , target )
        
        return results

mySolution = Solution()
print(mySolution.combinationSum([2,3,5], 8))
