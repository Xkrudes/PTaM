class Queue:
    def __init__(self):
        self.array = []
        self.size = 0
    def Getsize(self):
        return self.size
    def SetElement(self, index, data):
        if index >= 0 and index < self.size:
            self.array[index] = data
    def GetElement(self, index):
        if index >= 0 and index <= self.size:
            return self.array[index]

tmp = Queue()
tmp.array = [0, 1, 2, 3, 4]
tmp.size = 5
tmp.SetElement(5, 4)
print(tmp.array)
