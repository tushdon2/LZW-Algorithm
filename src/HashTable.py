class Node:
    def __init__(self, key, code):
        self.key = key
        self.code = code
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return "--"

        temp = self.head.next
        s = "(" + self.head.key + ", " + str(self.head.code) + ")"
        while temp != None:
            s += ", " + "(" + temp.key + ", " + str(temp.code) + ")"
            temp = temp.next
        return s

    def add(self, key, code):
        # adds a new node at the front of the linked list with key "key" and code "code"
        newNode = Node(key, code)
        newNode.next = self.head
        self.head = newNode

class HashTable:
    def __init__(self, length = 4096):
        self.length = length
        self.table = [LinkedList() for i in range(length)]        
        # for i in range(length): self.table.append(linkedList())

        self.items = 0
        # Initialise the hash table with first 256 unicode characters
        for i in range(256): self.add_element(chr(i))

    def __str__(self):
        s = str(self.table[0])
        for i in range(1, self.length):
            s += "\n" + str(self.table[i])
        return s
        
    def add_element(self, key):
        # uses chaining (open hashing) for collision resolution
        self.table[self.items % self.length].add(key, self.items)
        self.items += 1

if __name__ == "__main__":
    def hashf(n):
        return n % 5

    ht = HashTable(5)
    ht.add_element(hashf(10), 10)
    ht.add_element(hashf(5), 5)
    ht.add_element(hashf(3), 3)
    # print(ht)
    s = str(ht)
    print(s)

    # ll = linkedList()
    # ll.add(2)
    # ll.add(3)
    # ll.add(4)
    # print(ll)

