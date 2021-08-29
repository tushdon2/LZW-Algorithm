# http://rosettacode.org/wiki/LZW_compression#Python
# https://marknelson.us/posts/2011/11/08/lzw-revisited.html
import os
from hash_table import HashTable 

class LZW:
    def encode(self, input):
        # if not (os.path.exists(s) and os.path.isfile(s)): 
        #     print("wrong path")
        #     return
        
        # d = dict()
        # s1 = os.path.join(os.path.dirname(s), str(abs(hash(s))) + ".lzwtxt")
        ht = HashTable()
        pref = ""
        for i in input:
            npref = pref + i
            if ht.search(npref) != None: pref = npref
            else: 
                print(ht.search(pref))
                ht.add_element(npref)
                pref = i

        print(ht)

# class decode:
#     pass

if __name__ == "__main__":
    LZW().encode("tobeornottobeornot")
    