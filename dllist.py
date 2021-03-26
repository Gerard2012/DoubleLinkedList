class DLLNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.prev = prev
        self.nxt = nxt

    def __repr__(self):
        pval = self.prev and self.prev.value or None
        nval = self.nxt and self.nxt.value or None
        return f'[{repr(pval)}, {self.value}, {repr(nval)}]'


class DLList(object):

    def __init__(self):
        self.head = None
        self.end = None


    def push(self, obj):

        # Apends a new value to the end of the list.

        new_elem = DLLNode(obj, None, None)

        if self.head == None and self.end == None:
            self.head = new_elem
            self.end = self.head

        else:
            self.end.nxt = new_elem
            new_elem.prev = self.end
            self.end = new_elem


    def count(self):

        # Returns the number of items in the list.

        if not self.head:
            return 0

        else:
            x = 1
            n = self.head
            while n.nxt != None:
                x += 1
                n = n.nxt
            else:
                return x


    def traverse_list(self):

        # Return the contents of the list.

        if self.head == None:
            print('List is empty []')

        else:
            n = self.head
            while n != None:
                print(n)
                n = n.nxt


    def first(self):

        # Returns a reference for first item in list but does not remove it.

        if not self.head:
            return None

        else:
            return self.head.value


    def last(self):

        # Return last item in the list.

        if not self.head:
            return None

        else:
            return self.end.value


    def pop(self):

        # Removes the last item and returns it.

        if not self.head:
            return None

        elif self.head == self.end:
            n = self.end
            self.end = None
            self.head = None
            return n.value

        else:
            n = self.end
            new_end = self.end.prev
            new_end.nxt = None
            self.end = new_end
            return n.value


    def popleft(self):

        # Removes the first item and returns it.

        if not self.head:
            return None

        elif self.head == self.end:
            n = self.head
            self.end = None
            self.head = None
            return n.value

        else:
            n = self.head
            new_head = self.head.nxt
            new_head.prev = None
            self.head = new_head
            return n.value


    def remove(self, obj):

        # Finds a matching item and removes it from the list.

        if not self.head:
            print('List is empty[]')
            return False

        elif self.head.value == obj:
            self.head = self.head.nxt
            self.head.prev = None
            return True

        else:
            n = self.head
            while n.nxt != None:
                if n.nxt.value == obj:
                    n.nxt = n.nxt.nxt
                    if n.nxt == None:
                        pass
                    else:
                        n.nxt.prev = n
                    return True
                else:
                    print('Element not found in list[]')
                    return False


    def get(self, index):

        # Returns reference of item at given index.

        if not self.head:
            print('List is empty[]')

        elif index == 0:
            return self.head.value

        else:
            n = self.head
            node_assigned_index = 0
            while node_assigned_index < index:
                if not n.nxt:
                    return None
                else:
                    node_assigned_index += 1
                    n = n.nxt
            else:
                return n.value


    def dump(self):

        # Debugging func that dumps content of the list.

        if not self.head:
            print('List is empty[]')

        elif self.head and not self.head.nxt:
            return f'[{self.head.value}]'

        else:
            dump = f'['
            n = self.head
            while n.nxt != None:
                dump += n.value + ', '
                n = n.nxt
            else:
                dump += n.value + ']'

            return dump


if __name__ == '__main__':

    pass
