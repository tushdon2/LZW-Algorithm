# http://rosettacode.org/wiki/LZW_compression#Python
# https://marknelson.us/posts/2011/11/08/lzw-revisited.html
import os

# global length
# length = 4096

# def hashf(n):
#     return n % length

def encode(s):
    if not (os.path.exists(s) and os.path.isfile(s)): 
        print("wrong path")
        return
    
    d = dict()
    s1 = os.path.join(os.path.dirname(s), str(abs(hash(s))) + ".lzwtxt")



# class decode:
#     pass

# if __name__ == "__main__":
    # encode("Tushar Sahu")
    