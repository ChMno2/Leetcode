class Solution:
    def numberOfSteps(self, num: int) -> int:
        count =0 
        while num > 0:
            if num % 2 ==0 or num==1:
                count+=1
            elif num % 2 ==1:
                count+=2
            num//=2
        return count
            
