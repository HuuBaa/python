import struct

with open('test_struct.BMP','rb') as f:
    data=f.read(30)
b=struct.unpack('<ccIIIIIIHH', data)
if b[0]==b'B' and b[1]==b'M':
    print('size:',b[2],'color:',b[-1])