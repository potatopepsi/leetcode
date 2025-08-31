# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head) -> bool:
    visited = []

    while(head!=None):
        if(head in visited):
            return True
        visited.append(head)
        head = head.next

    return False

def main():
    #Test Case 1
    print("Test Case 1")
    #Test Case 2
    print("Test Case 2")
    #Test Case 3
    print("Test Case 3")

    

if __name__ == "__main__":
    main()
