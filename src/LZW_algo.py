# Resources:
# 1. http://rosettacode.org/wiki/LZW_compression#Python
# 2. https://marknelson.us/posts/2011/11/08/lzw-revisited.html
# 3. https://faculty.kfupm.edu.sa/ICS/saquib/ICS202/Unit32_LZW.ppt
# 4. Dynamic LZW for Compressing Large Files: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.217.7823&rep=rep1&type=pdf
# 5. On parsing optimality for dictionary-based textcompression — the Zip case: https://www.sciencedirect.com/science/article/pii/S1570866713000257
# 6. Improving LZW (data compression algorithm), R. Nigel Horspool: https://webhome.cs.uvic.ca/~nigelh/Publications/improvingLZW.pdf
# 7. The effect of non-greedy parsing in Ziv-Lempel compression methods, R. Nigel Horspool: https://ieeexplore.ieee.org/document/515520
# 8. The Relative Efficiency of Data Compression by LZW and LZSS, Yair Wiseman: https://pdfs.semanticscholar.org/ddf5/4749ad7d83dbe6ec17e88e5f4af6ac69c1c5.pdf

import os
from pathlib import Path
from hash_table import HashTable 

class LZWtext:
    def encode(self, inputPath):
        input = self.__input(inputPath) # gets input from file at location: 'inputPath'

        #--------------Main Encoding Algorithm--------------
        ht = HashTable(toEncode = True) # used as dictionary
        output = ""
        pref = ""
        for i in input:
            newPref = pref + i
            if ht.searchKey(newPref) != None: pref = newPref
            else: 
                output += str(ht.searchKey(pref)) + ','
                ht.addElement(newPref)
                pref = i
        output += str(ht.searchKey(pref))
        #--------------Main Encoding Algorithm--------------

        self.__output(inputPath, output, "encode") # stores output at "LZW/out/encode" directory

    def decode(self, inputPath):
        input = self.__input(inputPath, "decode") # gets input from file at location: 'inputPath'
      
        #------------Main Decoding Algorithm------------
        l = len(input)
        output = ""
        ht  = HashTable() # used as dictionary
        prevWord = ht.searchKey(input[0])
        output += prevWord
        prevChar = prevWord[0]
        for i in range(1, l):
            currentWord = ht.searchKey(input[i])
            if currentWord != None: String = currentWord
            else: String = prevWord + prevChar
            output += String
            prevChar = String[0]
            ht.addElement(prevWord + prevChar)
            if currentWord != None: prevWord = currentWord
            else: prevWord = ht.searchKey(input[i])
        #------------Main Decoding Algorithm------------

        self.__output(inputPath, output, "decode") # stores output at "LZW/out/decode" directory

    def __input(self, inputPath, way = None):
        # File Handling to get input from a file at 'inputPath'
        f = open(inputPath, "rt")
        input = f.read()
        if way == "decode": input = list(map(int, input.split(',')))
        f.close()
        return input

    def __output(self, inputPath, output = None, way = None):
        # File Handling to produce output 
        s = os.path.join(Path(__file__).parent.parent, "out")
        if not os.path.exists(s): os.mkdir(s)
        s = os.path.join(s, way)
        if not os.path.exists(s): os.mkdir(s)
        f = open(os.path.join(s, Path(inputPath).stem + "_" + way + ".txt"), "wt")
        f.write(output)
        f.close()
