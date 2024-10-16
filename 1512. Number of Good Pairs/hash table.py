#善用hash table紀錄每個數字出現的次數

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = {}
        count = 0
        for num in nums:
            count +=pair.setdefault(num,0)
            pair[num]+=1
        return count
