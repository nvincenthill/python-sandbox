from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
dequeued = queue.popleft()
print(dequeued)
dequeued = queue.popleft()
print(dequeued)
print(queue)
