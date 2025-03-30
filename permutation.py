class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        sample = []
        result = []
        hashmap = {

        }
       
        for i in nums:
            hashmap[i] = nums.count(i)
       
        def backtrack():
            if len(nums) == len(sample):
                
                result.append(sample[:])
                return
            for i in hashmap:
                if hashmap[i] > 0:
                    sample.append(i)
                    hashmap[i]-=1
                    backtrack()
                    sample.pop()
                    hashmap[i]+=1
                    
        backtrack()
        return result

       
mySolution = Solution()
print(mySolution.permuteUnique([1,1,2]))
        