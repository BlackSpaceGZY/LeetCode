import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from reverse import reverse
from test_singly_linked_list import *

"""
两数相加
解题思路:
使用单链表实现两数相加，需要考虑到以下几个方面：
1、两个链表的长度问题
2、进位问题
3、两链表长度相等，但产生进位问题
关于问题1，需要判断当前两个链表是否已全部遍历完
关于问题2，需要定义一个flag来保存进位（此处我使用两个进位标记，是因为我直接
把l1直接当成新表，来减少内存消耗（并没有什么用），需要在最之前记录此次的进位）
关于问题3，我们需要一个前驱节点来记录
结果:
执行用时:68 ms, 在所有 python3 提交中击败了99.55%的用户
内存消耗:13.8 MB, 在所有 python3 提交中击败了5.06%的用户
反思:
看了一些其他解题方法，大同小异。不过可以直接在第一个while循环就可以解决链表
长度不等问题，可以用两个实数值去等于此刻链表的值，若链表为空，则实数值为0，
这样标记也可以减少为1个，但前驱节点是必须存在的。
"""
class Solution:

	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
	    flag1, flag2 = 0, 0
	    L = l1
	    L_prev = None
	    while l1 != None and l2 != None:
	    	L_prev = l1 if L_prev==None else L_prev.next
	    	flag2 = (l1.val + l2.val + flag1) // 10
	    	l1.val = (l1.val + l2.val + flag1) % 10
	    	flag1 = flag2
	    	l1 = l1.next
	    	l2 = l2.next
	    if l2 != None:
	    	l1 = l2
	    	L_prev.next = l1
	    while l1 != None:
	    	flag2 = (l1.val + flag1) // 10
	    	l1.val = (l1.val + flag1) % 10
	    	flag1 = flag2
	    	l1 = l1.next
	    	L_prev = L_prev.next
	    if flag1 == 1:
	    	L_prev.next = ListNode(1)
	    return L	    
