from Crypto.Util.number import *
import string 

crctable = open('res', 'rb').read()

def crac(x, y):
    calc = (ord(x) ^ 0xff)*4
    # print(hex(calc))
    return (bytes_to_long(crctable[calc:calc+4][::-1]) ^ 0xffffff00)

compare = [
    0x77cde91a,
    0xccd2022f,
    0x608aeb79,
    0xfac5bd9d,
    0x8e7ea6e7,
    0x2d7a767a,
    0xb371dfac,
    0x712ab43b,
    0x35d048d6,
    0xf634d202,
    0x9a34568c,
    0xa904ff9a,
    0x83e7c438,
    0x620b9d61,
    0x5773afa9,
    0x664458b7,
    0xa43dd41,
    0xcee971dc,
    0xa9cc367a,
    0x6345ffb2,
    0x3ae7e1f9,
    0x2c90f1f8,
    0x3b619b06,
    0x2690dd53,
    0x1bf8ef9b,
    0x2ac998a9,
    0x2031aaf1,
    0x69e0f85,
    0xaa9d940f,
    0x3712e66b,
    0x45e38f79,
    0x3b4ba1c1,
    0x196f7aea,
    0xf4523f88,
    0xadcc08c0,
    0xaab631e6,
    0x6f5bc681,
    0x7e2c6f8f,
    0x256b08cc,
    0xe5cf91f8,
    0xe2b9bb1e,
    0xa75f4fb9,
    0x65182448,
    0x48948c8, ]

res = ''
chars = string.printable

for _ in range(44):
    for idx in range(len(chars)):
        input = res + chars[idx]
        benar = False
        for i in range(len(input)):
            c = 0
            for j in range(0, i+1):
                c += crac(input[j], 1)
            if compare[i] == c & 0xffffffff:
                benar = True
                # print('benar', end='')
            else:
                benar = False
                # print('salah', end='')
        if benar:
            print(chars[idx], end='')
            res += chars[idx]
            break

