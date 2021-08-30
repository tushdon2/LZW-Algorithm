class HashTable:
    # Hash Table to be used as dictionary in LZW Algorithm
    # Uses chaining (open hashing) for collision resolution

    # Nested Class: _LinkedList
    class _LinkedList:
        # Nested Class: _Node
        class _Node:
            def __init__(self, key, code):
                self.key = key
                self.code = code
                self.next = None

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
            # Adds a new node at the front of the linked list with key "key" and code "code"
            newNode = self._Node(key, code)
            newNode.next = self.head
            self.head = newNode

        def getCode(self, key, _node):
            # Recursive function to search for a key in the Linked List and return the respective code if the key exists, else to return 'None'
            if _node != None:
                if _node.key == key: return _node.code
                else: return self.getCode(key, _node.next)
            return None

    def __init__(self, length = 4096, toEncode = False):
        self.length = length # length of the hash table
        self.table = [self._LinkedList() for i in range(length)]        
        self.items = 0 # items currently present in the hash table
        self.toEncode = toEncode # if true then hash table set for encoding, else it is set for decoding
        for i in range(256): self.add_element(chr(i)) # initialise the hash table with first 256 UNICODE characters

    def __str__(self):
        s = str(self.table[0])
        for i in range(1, self.length):
            s += "\n" + str(self.table[i])
        return s
        
    def hashFunc(self, key):
        # Hashes a given key by:
        # 1. summing up the UNICODE values of the individual characters of the key and then taking modulo length if encoding
        # 2. taking ( key modulo length ) if decoding 
        if self.toEncode:
            hashValue = 0
            for i in key: hashValue += ord(i)
        else: hashValue = key
        hashValue %= self.length
        return hashValue

    def add_element(self, toAdd):
        if self.toEncode: 
            # While encoding 'key' is the string and 'code' is its respective item number
            key = toAdd
            code = self.items
        else: 
            # While decoding 'key' is the item number and 'code' is the string to be stored
            code = toAdd
            key = self.items
        self.table[self.hashFunc(key)].add(key, code)
        self.items += 1
    
    def searchKey(self, key):
        ll = self.table[self.hashFunc(key)]
        return ll.getCode(key, ll.head)

if __name__ == "__main__":
    ht = HashTable(25)
    ht.add_element("mkv")
    
    print(ht)
    print(ht.search('mkv'))
