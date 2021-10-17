from exceptions import Empty

class LinkedList():
    class _Node():
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, element):
        newest = self._Node(element, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
        self._head = newest
        self._size += 1

    def add_last(self, element):
        newest = self._Node(element, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        self._tail._next = newest
        newest._next = None
        self._tail = newest
        self._size += 1

    def add_any(self, element, position):
        newest = self._Node(element, None)
        temp_head = self._head
        i = 1
        if self.is_empty():
            self._head = newest
            self._tail = newest
        while i < position:
            temp_head = temp_head._next
            i += 1
        newest._next = temp_head._next
        temp_head._next = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('The linked list is empty.')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value


    def remove_last(self):
        if self.is_empty():
            raise Empty('The linked list is empty.')
        temp_head = self._head
        i = 0
        while i < len(self) - 2:
            temp_head = temp_head._next
            i += 1
        self._tail = temp_head
        temp_head = temp_head._next
        value = temp_head._element
        self._tail._next = None
        self._size -= 1
        return value

    def remove_any(self, position):
        if self.is_empty():
            raise Empty('The linked list is empty.')
        temp_head = self._head
        i = 1
        while i < position - 1:
            temp_head = temp_head._next
            i += 1
        value = temp_head._next._element
        temp_head._next = temp_head._next._next
        self._size -= 1
        return value

    def display(self):
        temp_head = self._head
        while temp_head:
            print(temp_head._element, end='-->')
            temp_head = temp_head._next
        print()

a_linked_list = LinkedList()
a_linked_list.add_last(10)
a_linked_list.add_last(20)
a_linked_list.add_last(30)
a_linked_list.add_last(40)
a_linked_list.add_last(50)
a_linked_list.display()
a_linked_list.add_any(60, 3)
a_linked_list.display()
a_linked_list.remove_first()
a_linked_list.display()