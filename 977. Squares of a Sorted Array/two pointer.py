#給定一個list，回傳square後的list
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p1 = 0
        p2 = len(nums)-1
        ans =[]
        while p1<=p2:
            if abs(nums[p1])<abs(nums[p2]):
                ans.append(nums[p2]**2)
                p2-=1
            else: 
                ans.append(nums[p1]**2)
                p1+=1
        return ans[::-1]
