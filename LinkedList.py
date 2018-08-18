class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,element):
        current=self.head

        if not self.head:
            self.head=element
        else:
            while current.next:
                current=current.next
            current.next=element


