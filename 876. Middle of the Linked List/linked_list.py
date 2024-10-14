#利用兩個pointer移動的速度差，造成快的pointer到達結束時，慢的pointer跑到中間
#fast 一次移動兩個 slow一次移動一個
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
