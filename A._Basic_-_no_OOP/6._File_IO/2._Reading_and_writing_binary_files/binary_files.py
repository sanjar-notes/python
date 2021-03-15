a = 65534 # FF FE
b = 65535 # FF FF
c = 65536 # 00 01 00 00
d = 2998302  # 02 2D C0 1E
with open('binary2', 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'little'))

with open('binary2', 'br') as bin_file:
    a = int.from_bytes(bin_file.read(2), 'big')
    print(a)
    b = int.from_bytes(bin_file.read(2), 'big')
    print(b)
    c = int.from_bytes(bin_file.read(4), 'big')
    print(c)
    d = int.from_bytes(bin_file.read(4), 'big')
    print(d)
    d = int.from_bytes(bin_file.read(4), 'big')
    print(d)
