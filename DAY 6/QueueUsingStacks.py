# Enter your code here. Read input from STDIN. Print output to STDOUT

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None

if __name__ == "__main__":
    q = int(input()) 
    queue = Queue()
    for _ in range(q):
        query = input().split()

        query_type = int(query[0])

        if query_type == 1:
            x = int(query[1])
            queue.enqueue(x)
        elif query_type == 2:
            queue.dequeue()
        elif query_type == 3:
            front_element = queue.front()
            print(front_element)
