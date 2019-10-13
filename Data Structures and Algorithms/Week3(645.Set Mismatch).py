class Solution:
 
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        nnums = set(nums)
        N = len(nums) 
        missing = N*(N+1)/2-sum(nnums)   #計算缺失值
        
        duplicated = sum(nums) - sum(nnums)  #計算重複值
                
        return [duplicated,int(missing)]
