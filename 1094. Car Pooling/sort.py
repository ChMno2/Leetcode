#將上車與下車人數做成一個list並排序，並依從先下車後上車的原理
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        schedule = []
        for trip in trips:
            schedule.append([trip[1], trip[0]])
            schedule.append([trip[2], -trip[0]])
        schedule.sort()
        curr = 0
        for _, passenger in schedule:
            curr +=passenger
            if curr > capacity:
                return False
        return True
            
