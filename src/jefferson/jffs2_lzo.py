import lzo
import struct

def decompress(data, size):
    return lzo.decompress("\xf0" + struct.pack("!I", size) + data)
