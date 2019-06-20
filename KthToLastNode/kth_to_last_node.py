class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None



def kth_to_last_node(num, ll):
# ll.value is the head of the list
# iterate over the whole list and get length .. create counter variable and increase by 1
# subtract int from total length to get amount of times to iterate over list again
# while i < new value, move through the list with .next
# return value that exists at the new value's position

    node = ll

    length = 1
    second_iter = 0
    while node.next is not None:
        length += 1
        node = node.next

    second_iter = (length - num) + 1

    node = ll
    counter = 1

    while counter < second_iter:
        node = node.next
        counter += 1
    
    return node.value

    





a = ListNode("Australian Sheperd")
b = ListNode("Beagle")
c = ListNode("Cairne Terrier")
d = ListNode("Dobermann")
e = ListNode("English Mastiff")

a.next = b
b.next = c
c.next = d
d.next = e



print(kth_to_last_node(2, a))