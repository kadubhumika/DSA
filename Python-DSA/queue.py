class MyStack(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

        size = len(self.queue)
        for i in range(size - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0
