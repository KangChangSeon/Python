# Node 클래스
class Node:
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next



# 연결리스트 클래스
class LinkedList:
    
    def __init__( self ):
        self.head = None

    
    def isEmpty( self ): return self.head == None
    def isFull( self ): return False

    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head;
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :         
            self.head = Node(elem, self.head)
        else :
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :         
            if self.head is not None :
                self.head = self.head.link
        elif before.link != None :
            before.link = before.link.link

    # 추가 연산들
    def size( self ) :
        node = self.head;
        count = 0;
        while node is not None :
            node = node.link
            count += 1
        return count

    def __str__( self ) :
        arr = []
        node = self.head
        while node is not None :
            arr.append(node.data)
            node = node.link
        return str(arr)
    

    def replace(self, pos, elem) :
        node = self.getNode(pos)
        if node != None : node.data = elem

    def find(self, val) :
        node = self.head;
        while node is not None:
            if node.data == val : return node
            node = node.link
        return node


#======================================================================
if __name__ == "__main__":
    L = LinkedList()
    
    print("최초   ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(3, 40)
    L.insert(2, 50)
    print(L)
    L.delete(2)
    print("삭제(2)", L)
    L.delete(3)
    print("삭제(3)", L)
    L.delete(0)
    print("삭제(0)", L)

