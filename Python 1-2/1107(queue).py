class CircularQueue:
    #큐의 생성자, 큐의 용량을 전달받아 이 크기의 큐를 위한 데이터를 선언하고 초기화 함
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0
    
    def isEmpty(self):
        # front와 rear가 같으면 공백상태
        return self.front == self.rear
    
    def isFull(self):
        #front가 rear의 다음 위치이면 포화 상태
        return self.front == (self.rear+1)%self.capacity
    
    # 포화가 아니면 삽입 가능
    # 1. rear를 시계방향으로 회전시키고
    # 2. 그 위치에 새로운 요소를 저장
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % self.capacity
            self.array[self.rear] = item
        else: pass

    # 공백이 아니면 삭제 가능
    # 1. front를 회전시키고
    # 2. 그 위치의 요소를 반환
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % self.capacity
            return self.array[self.front]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)% self.capacity]
        else: pass

    # 전체 요소의 수 : (rear - front + capacity) % capacity
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def __str__(self):
        if self.front < self.rear:
            # front<rear 이면 front+1 부터 rear까지의 요소를 출력, 슬라이싱 기능을 이용
            return str(self.array[self.front+1:self.rear+1])
        else:
            # 그렇지 않으면, 두 부분을 나누어 출력함. front+1 ~ capacity-1 까지와 0~rear까지임
            return str(self.array[self.front+1:self.capacity]+ self.array[0:self.rear+1])
        
q = CircularQueue(5)
q.enqueue('B')
q.enqueue('C')

q.enqueue('A')
q.enqueue('D')
q.dequeue()
q.enqueue('E')
q.dequeue()
print(q)
for i in rang