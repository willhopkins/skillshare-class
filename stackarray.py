# We generated our own exceptions class.
from exceptions import Empty


class ArrayStack:
    def __init__(self):
        self._data = []

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]


stack = ArrayStack()
stack.push(10)
stack.push(20)
print('Stack: ', stack._data)
print('Length: ', stack.len())
print('Is it empty? ', stack.is_empty())
print('Popped: ', stack.pop())
print('Popped: ', stack.pop())
print('Is it empty? ', stack.is_empty())
stack.push(30)
stack.push(40)
print('On top is: ', stack.top())
