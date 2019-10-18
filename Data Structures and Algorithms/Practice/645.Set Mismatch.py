class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        for i in set(nums):
            dict[i] = nums.count(i)  #計算nums裡各元素的出現次數
    
        truesum = 0
        for n in range(len(nums)+1):
            truesum = truesum + n    #計算正確set的總和
    
        for num in nums:
            if dict[num] == 2:
                a = num              #找出重複出現的元素
    
        sum = 0
        for i in dict.keys():
            sum = sum + i
        b = truesum - sum            #找出缺失的元素           
                
        return [a,b]
    
