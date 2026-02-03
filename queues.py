import random
class Queue:
    def __init__(self,size):
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        self.size = size 
    def enqueue(self,value):
        if self.rear < self.size:
            self.queue[self.rear] = value
            self.rear+=1
        else:
            print("queue overflow")
    def dequeue(self):
        if self.front<=self.rear:
            self.queue[self.front] = None
            self.front+=1
        else:
            print("queue underflow")

q = Queue(12)
for i in range(12):
    q.enqueue(random.randint(1,10))
    print(q.rear,"rear")
print(q.queue)
for i in range(5):
    q.dequeue()
    print(q.front,"front")

