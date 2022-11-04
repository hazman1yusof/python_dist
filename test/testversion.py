# First import struct module.
import struct 

# Return 64 means 64-bit version, return 32 means 32-bit version.
version = struct.calcsize("P")*8 

print(version)