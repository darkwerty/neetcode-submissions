class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1

        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        resized_arr = [0] * self.capacity

        for i in range(0, self.size):
            resized_arr[i] = self.arr[i]
        
        self.arr = resized_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity