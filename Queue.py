class Queue():
    def __init__(self):
        self.length = 0
        self.head = 0
        self.tail = 0
        self.max_cap = 3
        self.queue_array = [0] * self.max_cap

    def __str__(self):
        string = ""
        for i in range(self.length):
            string += "[" + str(self.queue_array[(self.head + i) % self.max_cap]) + "]"
        return string

    def enqueue(self, element):
        if self.length == self.max_cap:
            print("Queue overflow")
            return
        self.queue_array[self.tail] = element
        self.tail = (self.tail + 1) % self.max_cap
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            print("Queue underflow")
            return
        element = self.queue_array[self.head]
        self.head = (self.head + 1) % self.max_cap
        self.length -= 1
        return element
