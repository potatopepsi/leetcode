# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(head):
    
    track=[]

    while(head!=None):
        track.append(head)
        head = head.next
    
    nodeLength = len(track)
    if(nodeLength%2==0):
        return track[-(-nodeLength//2)]
    else:
        return track[(-(-nodeLength//2))-1]

        