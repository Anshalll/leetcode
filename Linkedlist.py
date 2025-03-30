class Node():
    def __init__(self , data):
        self.next = None
        self.data = data

class LinkedList():
    def __init__(self):
            self.head= None
        
    def AddSequence(self , data):
      
        current = Node(data)
        current.next = self.head
        self.head = current

    def iterate(self):
             temp = self.head
             while temp is not None:
                   print(temp.data , end="->")
                   temp = temp.next
             print("none")
    def getAtIndex(self , index):
          temp = self.head
          count = 0

          while temp is not None:
                if count == index:
                      return temp.data
                temp = temp.next
                count+=1    
    def appendAtIndex(self, index, data):
        new_node = Node(data)
        if index == 0:
            
            new_node.next = self.head
            self.head = new_node
        count = 0
        temp = self.head

        while temp is not None and count < index - 1:
             temp = temp.next
             count +=1
        
        new_node.next = temp.next
        temp.next = new_node
        

mylinkedlist = LinkedList()
mylinkedlist.AddSequence(10)
mylinkedlist.AddSequence(20)
mylinkedlist.AddSequence(30)
mylinkedlist.AddSequence(40)


mylinkedlist.appendAtIndex(1 , 9)


mylinkedlist.iterate()
# print(mylinkedlist.getAtIndex(0))