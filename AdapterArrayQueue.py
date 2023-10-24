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

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        return " -> ".join(map(str, self.array))

    def SetElement(self, index: int, data: int):
        if index >= 0 and index < self.size:
            self.array[index] = data
    
    def __getitem__(self, index: int) -> int:
            return self.array[index]

if __name__ == '__main__':
    array = ArrayQueue()
    array.enqueue(1)
    array.enqueue(2)
    array.enqueue(3)
    print(array)