'''
Traverse the whole list and store each value in a stack
Traverse the list again
  Pop off the last value in the stack and compare it to the first value
  Keep going for each value -- if true, continue if not, return false
  When the second traversal gets to the end of the list and everything matches, return true
'''
class ListNode:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node 

def isLinkedListPalindrome(node):

    stack = []
    traversing = node

    while traversing:
        stack.append(traversing.value)
        if traversing.next_node:
            traversing = traversing.next_node
        else:
             break
    print(stack)
    while len(stack) > 0:
      comparer = stack.pop()
      if node.value == comparer:
          node = node.next_node
      else:
          return False

    return True

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

w = ListNode(10)
x = ListNode(11)
y = ListNode(11)
z = ListNode(10)

w.next_node = x
x.next_node = y
y.next_node = z

print(isLinkedListPalindrome(a))   # should print true
print(isLinkedListPalindrome(b))   # should print false since now the 'a' node is not included in the linked list

print(isLinkedListPalindrome(w))   # should print true