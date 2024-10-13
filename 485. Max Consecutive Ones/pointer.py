class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ones = 0
        for i in nums:
            if i==1:
                count+=1
            else:
                count=0
            max_ones = max(max_ones,count)
        
        return max_ones
