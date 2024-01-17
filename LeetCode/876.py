'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.  '''

def middleNode(head):
    x = len(head) 
    head = head[x//2:]
    print(head)

list = [1,2,3,4,5,6]
middleNode(list) #The result needs to be [4,5,6]