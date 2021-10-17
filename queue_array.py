from exceptions import Empty

class ArrayQueue:
    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, element):
        self._data.append(element)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._front += 1
        self._size -= 1
        return value

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]


my_queue = ArrayQueue()
print(my_queue.is_empty())
my_queue.enqueue(10)
my_queue.enqueue(20)
print(my_queue.is_empty())
print(my_queue.first())
print('Dequeueing: ', my_queue.dequeue())
print(my_queue.is_empty())
print(my_queue.first())