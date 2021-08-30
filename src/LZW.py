# Resorces:
# 1. http://rosettacode.org/wiki/LZW_compression#Python
# 2. https://marknelson.us/posts/2011/11/08/lzw-revisited.html
# 3. https://faculty.kfupm.edu.sa/ICS/saquib/ICS202/Unit32_LZW.ppt
# 4. Dynamic LZW for Compressing Large Files: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.217.7823&rep=rep1&type=pdf
# 5. On parsing optimality for dictionary-based textcompression — the Zip case: https://www.sciencedirect.com/science/article/pii/S1570866713000257
# 6. Improving LZW (data compression algorithm), R. Nigel Horspool: https://webhome.cs.uvic.ca/~nigelh/Publications/improvingLZW.pdf
# 7. The effect of non-greedy parsing in Ziv-Lempel compression methods, R. Nigel Horspool: https://ieeexplore.ieee.org/document/515520
# 8. The Relative Efficiency of Data Compression by LZW and LZSS, Yair Wiseman: https://pdfs.semanticscholar.org/ddf5/4749ad7d83dbe6ec17e88e5f4af6ac69c1c5.pdf

import os
from hash_table import HashTable 

class LZW:
    def encode(self, input):
        # if not (os.path.exists(s) and os.path.isfile(s)): 
        #     print("wrong path")
        #     return
        
        # d = dict()
        # s1 = os.path.join(os.path.dirname(s), str(abs(hash(s))) + ".lzwtxt")
        ht = HashTable(toEncode = True)
        pref = ""
        for i in input:
            npref = pref + i
            # print(pref, i, npref)
            if ht.searchKey(npref) != None: pref = npref
            else: 
                print(ht.searchKey(pref))
                ht.add_element(npref)
                pref = i
            # print("--------------------------")
        print(ht.searchKey(pref))
        # print(ht)

    def decode(self, input):
        input = [int(x) for x in input.split()]
        l = len(input)
        output = ""
        ht  = HashTable()
        prevWord = ht.searchKey(input[0])
        output += prevWord
        prevChar = prevWord[0]
        for i in range(1, l):
            currentWord = ht.searchKey(input[i])
            if currentWord != None: String = currentWord
            else: String = prevWord + prevChar
            output += String
            prevChar = String[0]
            ht.add_element(prevWord + prevChar)
            prevWord = currentWord
        print(output)

if __name__ == "__main__":
    s1 = "116 111 98 101 111 114 110 111 116 256 258 260 262 116"
    # LZW().encode("tobeornottobeornot")
    LZW().decode(s1)
    # print([x for x in s1.split()])
    