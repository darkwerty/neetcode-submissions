class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        if index == 0 and self.head.next == None:
            return -1

        i = 0
        ref = self.head.next

        while ref and i < index:
            ref = ref.next
            i += 1

        if i != index or ref == None: return -1 # Index out of bounds
        
        return ref.val
        

    def insertHead(self, val: int) -> None:
        # Create new head node
        newHead = ListNode(val, self.head.next)

        if self.head == self.tail:
            self.tail = newHead
        self.head.next = newHead

    def insertTail(self, val: int) -> None:
        newTail = ListNode(val)
        self.tail.next = newTail
        self.tail = newTail
        
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr.next:
            curr = curr.next
            i += 1
        
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        nodeList = []

        ref = self.head.next

        while ref:
            nodeList.append(ref.val)
            ref = ref.next

        #nodeList.append(ref.val)

        return nodeList
        



  
