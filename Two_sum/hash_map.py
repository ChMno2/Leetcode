# [2,7,11,15] target = 9
# diff = [[9-i],idx]......]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {} #key:diff , value: index
        for idx,num in enumerate(nums):
            if diff.get(num,None) == None:
                diff[target-num] = idx
            else:
                return [diff[num],idx]
