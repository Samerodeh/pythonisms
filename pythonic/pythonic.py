from functools import wraps

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, col = None):
        self.head = None
        self._length = 0
        if col:
            for item in reversed(col):
                self.insert(item)

    def traverse(self, action):
        curr = self.head
        while curr:
            action(curr.val)
            curr = curr.next

    def __iter__(self):
        def generator():
            curr = self.head
            while curr:
                yield curr.val
                curr = curr.next
        return generator()

    def __str__(self):
        output = ''
        for val in self:
            output += f'[{val}] -> '
        return output + 'None'

    def __len__(self):
        return self._length

    def insert(self, val):
        self.head = Node(val, self.head)
        self._length += 1

    def __getitem__(self, idx):
        if idx < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == idx:
                return item
        raise IndexError

def proclaim(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        orig_val = function(*args, **kwargs)
        return 'I want to say, ' + orig_val
    return wrapper

@proclaim
def txt(message):
    return message

if __name__ == '__main__':
    print(txt('Hello World.'))