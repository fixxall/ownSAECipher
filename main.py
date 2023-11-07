import binascii


class OWNSAE:
    def __init__(self, XorKey, ShiftKey1, ShiftKey2):
        self.ShiftKey1 = ShiftKey1
        self.ShiftKey2 = ShiftKey2
        self.XorKey = XorKey
        self.round = 17

    def BitsPad8(self, x):
        if(len(x)%8==0): return x
        bits = (8-(len(x)%8))*'0' + x
        return bits

    def BytesToBits(self, x):
        count = int.from_bytes(x, "big")
        bits = bin(count)[2:]
        bits = self.BitsPad8(bits)
        return bits
    
    def BitsToBytes(self, x):
        count = int(x, 2)
        byt = count.to_bytes(len(x)//8,"big")
        return byt

    def xorBits(self, a, b):
        ret = ''
        for i, j in zip(a,b):
            if(i!=j): ret += '1'
            else: ret += '0'
        return ret

    def shifterRight(self, x, key):
        ll = len(x)
        key = key%ll
        ret = x[key:] + x[:key]
        return ret 

    def shifterLeft(self, x, key):
        ll = len(x)
        key = key%ll
        ret = x[-key:] + x[:-key]
        return ret 

    def encrypt(self, message):
        mbits = self.BytesToBits(message)
        kbits = self.BytesToBits(self.XorKey)
        rang = len(mbits)//len(kbits)
        kbits = (kbits*(rang+1))[:len(mbits)]
        
        mbits = self.xorBits(mbits, kbits)
        for i in range(self.round-1):
            mbits = self.shifterRight(mbits, self.ShiftKey1)
            kbits = self.shifterRight(kbits, self.ShiftKey2)
            mbits = self.xorBits(mbits, kbits)
        # print(mbits)
        return binascii.hexlify(self.BitsToBytes(mbits)).decode()

    def decrypt(self, message):
        message = binascii.unhexlify(message)
        mbits = self.BytesToBits(message)
        kbits = self.BytesToBits(self.XorKey)
        rang = len(mbits)//len(kbits)
        kbits = (kbits*(rang+1))[:len(mbits)]
        
        # print(mbits)
        kkey = [kbits]
        for i in range(self.round-1):
            kbits = self.shifterRight(kbits, self.ShiftKey2)
            kkey.append(kbits)
        kkey = kkey[::-1]

        mbits = self.xorBits(mbits, kkey[0])
        kkey = kkey[1:]
        for i in range(self.round-1):
            mbits = self.shifterLeft(mbits, self.ShiftKey1)
            mbits = self.xorBits(mbits, kkey[i])
        
        return self.BitsToBytes(mbits).decode()



def menus():
    ans = '''
SELAMAT DATANG PETUALANG
INI ENKRIPSI BARU LHO
!!!!!!!!!!!!!!!!!!!!!!!!
'''
    print(ans)

def options():
    print("1.Enc message\n2.Dec message\n3.Exit")

if __name__ == "__main__":
    menus()
    own = OWNSAE(b'keykeykeykeykey', 17, 91)
    assert own.shifterLeft(own.shifterRight('11000101001',4),4)=='11000101001'
    while(True):
        options()
        inp = input("Choice: ").strip()
        if(inp=='1'):
            plain = input("Your plaintext in utf: ")
            print("ciphertext is:", own.encrypt(plain.encode()))
        elif(inp=='2'):
            cipher = input("Your ciphertext hex: ")
            print("plaintext is:", own.decrypt(cipher))
        elif(inp=="3"):
            break
        else: print("Invalid input!!")