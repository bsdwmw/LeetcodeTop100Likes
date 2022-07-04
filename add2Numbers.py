'''Problem Description: https://leetcode.com/problems/add-two-numbers/'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(l1, l2):
      dummy = ListNode(0, None)
      dummyHead = dummy # to return
      carry = 0

      while l1 != None and l2 != None: # When l1 and l2 are not None
          num = l1.val + l2.val + carry
          new = ListNode(num % 10)
          dummy.next = new
          carry, dummy = num // 10, new
          l1, l2 = l1.next, l2. next

      if l1 != None: temp = l1 # When either l1 or l2 is None
      else: temp = l2
      while temp != None: 
          num = temp.val + carry
          new = ListNode(num % 10)
          dummy.next = new
          carry = num // 10
          temp, dummy = temp.next, new

      if carry != 0: dummy.next = ListNode(carry, None) # Check if carry remains
      return dummyHead.next

# Use divmod() to make the code more elegant
def addTwoNumbers(l1, l2):
      dummy = ListNode(0, None)
      dummyHead = dummy # to return
      carry = 0

      while l1 != None and l2 != None: 
          carry, num = divmod(l1.val + l2.val + carry, 10)
          new = ListNode(num)
          dummy.next = new
          dummy = new
          l1, l2 = l1.next, l2. next

      if l1 != None: temp = l1 
      else: temp = l2
      while temp != None: 
          carry, num = divmod(temp.val + carry, 10)
          new = ListNode(num)
          dummy.next = new
          temp, dummy = temp.next, new

      if carry != 0: dummy.next = ListNode(carry, None) 
      return dummyHead.next
