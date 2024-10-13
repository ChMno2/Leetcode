
#[2,7,11,15] target=18
# init = [(2,0)(7,1)(11,2)(15,3)]
# sort = [(2,0)(11,2)(7,1)(15,3)]
# 如果左加右小於target，則left++
# 如果左加右大於target，則right

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = list(zip(nums,range(len(nums))))
        num_index.sort()
        left = 0
        right = len(num_index) -1
        while left < right:
            curr_sum = num_index[left][0]+num_index[right][0]
            if curr_sum == target:
                return [num_index[left][1],num_index[right][1]]
            elif curr_sum < target:
                left+=1
            else:
                right-=1
