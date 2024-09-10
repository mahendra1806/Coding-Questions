class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b==0:
                return abs(a)
            return gcd(b,a%b)
        if not head:
            return head
        current=head
        
        while current and current.next:
            next_node=current.next
            gcd_value=gcd(current.val,next_node.val)
            new_node=ListNode(gcd_value)
            current.next=new_node
            new_node.next=next_node
            current=next_node
        return head
