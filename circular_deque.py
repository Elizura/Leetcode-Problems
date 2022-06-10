class MyCircularDeque:

    def __init__(self, k: int):
        self.MyCircularDeque=[]
        self.size=k
    def insertFront(self, value: int) -> bool:
        if self.size:
            self.MyCircularDeque.insert(0,value)
            self.size-=1
        else:
            return False
        return True
    def insertLast(self, value: int) -> bool:
        if self.size:
            self.MyCircularDeque.append(value)
            self.size-=1
        else:
            return False
        return True

    def deleteFront(self) -> bool:
        if self.MyCircularDeque:
            self.MyCircularDeque.pop(0)
            self.size+=1
        else:
            return False
        return True
    def deleteLast(self) -> bool:
        if self.MyCircularDeque:
            self.MyCircularDeque.pop()
            self.size+=1
        else:
            return False
        return True
    def getFront(self) -> int:
        if self.MyCircularDeque:
            return self.MyCircularDeque[0]
        else:
            return -1
    def getRear(self) -> int:
        if self.MyCircularDeque:
            return self.MyCircularDeque[-1]
        else:
            return -1    
    def isEmpty(self) -> bool:
        return not self.MyCircularDeque
    def isFull(self) -> bool:
        return not self.size
        
