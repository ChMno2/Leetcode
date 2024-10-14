#同時利用max1和max2分別儲存最大值與第二大值，避免使用兩次for loop


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = 0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2: 
                max2 = num
        return (max1-1)*(max2-1)
