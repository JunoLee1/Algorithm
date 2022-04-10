#Definition for singly-linked list
class ListNode:
  def __init__(self,val,next):
    self.val =  val
    self.next = next

def mergeTwoLists(list1,list2):
    dummyNode = ListNode(0)
    runner = dummyNode
    while list1 or list2 :
        if list1 is list2 :
            runner.next = list2 
            list2 = list2.next
        elif list2 is None:
            runner.next = list1
            list1 =list1.next
        else:
            if list1.val < list2.val:
                runner.next = list1
                list1 = list1.next
            else :
                runner.next = list2
                list2 = list2.next
            runner = runner.next
    return dummyNode.next
list11 = [1,2,4]
list22 = [1,3,4] 
print(mergeTwoLists(list11,list22))

