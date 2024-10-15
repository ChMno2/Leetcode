#將數字取log10,回傳為奇數時，該數字原來即為奇數位數

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x:int(log10(x)) % 2 ==1 ,nums)))
