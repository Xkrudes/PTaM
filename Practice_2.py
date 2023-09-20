class ArrayQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        self.array.append(data)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Очередь пуста")
        self.size -= 1
        return self.array.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Очередь пуста")
        return self.array[0]

    def size(self):
        return self.size

    def __str__(self):
        return " -> ".join(map(str, self.array))

    def SetElement(self, index, data):
        if index >= 0 and index < self.size:
            self.array[index] = data
    
    def GetElement(self, index):
        if index >= 0 and index <= self.size:
            return self.array[index]

if __name__ == '__main__':
    pass
