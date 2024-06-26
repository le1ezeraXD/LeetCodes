'''给定链表 head 和两个整数 m 和 n. 遍历该链表并按照如下方式删除节点:

开始时以头节点作为当前节点.
保留以当前节点开始的前 m 个节点.
删除接下来的 n 个节点.
重复步骤 2 和 3, 直到到达链表结尾.
在删除了指定结点之后, 返回修改过后的链表的头节点.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #使用双指针
    def deleteNodes(head, m: int, n: int):
        #定义快慢两个指针指向头节点
        currentNode = head
        lastMNode = head
        #当慢节点不为空时
        while currentNode != None:
            #初始化两个m,n来做遍历时的处理
            mCount = m
            nCount = n
            #遍历m次，使指针向前走到即将被删除的节点的前一个节点
            while currentNode != None and mCount != 0:
                #使用lastMNode记录当前节点
                lastMNode = currentNode
                #慢节点后移一位
                currentNode = currentNode.next
                mCount -= 1

            #同理，该处的作用是遍历n次来跳过要删除的节点
            while currentNode != None and nCount != 0:
                currentNode = currentNode.next
                nCount -= 1
            lastMNode.next = currentNode
        return head