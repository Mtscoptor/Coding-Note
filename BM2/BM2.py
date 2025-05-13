class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        #先添加头结点
        res = ListNode(-1)
        res.next = head
        pre = res

        #将pre移至m-1处
        for i in range(1,m):
            pre = pre.next
        cur = pre.next

        #每次循环都将temp所在位置的元素塞到m-1位置的后面，每个循环完成一次完整的位置转换
        for j in range(m,n):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return res.next