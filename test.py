from main import OWNSAE
own = OWNSAE(b'keykeykeykeykey', 17, 91)

import pytest

def test_Test1_BitsPad8():
    assert own.BitsPad8("110101010001010010001") == "000110101010001010010001","test failed" 
def test_Test2_BitsPad8():
    assert own.BitsPad8("123213214214") == "Input tidak valid","test failed" 
def test_Test3_BitsPad8():
    assert own.BitsPad8("") == "","test failed" 

def test_Test1_BytesToBits():
    assert own.BytesToBits(b"testing") == "01110100011001010111001101110100011010010110111001100111","test failed" 
def test_Test2_BytesToBits():
    assert own.BytesToBits(930981323) == "Input tidak valid","test failed" 
def test_Test3_BytesToBits():
    assert own.BytesToBits(b"") == "","test failed" 

def test_Test1_BitsToBytes():
    assert own.BitsToBytes("01110100011001010111001101110100011010010110111001100111") == b"testing","test failed" 
def test_Test2_BitsToBytes():
    assert own.BitsToBytes("123213214214") == "Input tidak valid","test failed" 
def test_Test3_BitsToBytes():
    assert own.BitsToBytes("") == "","test failed" 

def test_Test1_xorBits():
    assert own.xorBits("11111001001100010","10010001011000000") == "01101000010100010","test failed" 
def test_Test2_xorBits():
    assert own.xorBits("!32314124242c2c",3423423) == "Input tidak valid","test failed" 
def test_Test3_xorBits():
    assert own.xorBits("","") == "","test failed" 

def test_Test1_shifterRight():
    assert own.shifterRight("111001001001110010",4) == "010010011100101110","test failed" 
def test_Test2_shifterRight():
    assert own.shifterRight("1322323") == "Input tidak valid","test failed" 
def test_Test3_shifterRight():
    assert own.shifterRight("",0) == "","test failed" 

def test_Test1_shifterLeft():
    assert own.shifterLeft("010010011100101110",4) == "111001001001110010","test failed" 
def test_Test2_shifterLeft():
    assert own.shifterLeft("1322323") == "Input tidak valid","test failed" 
def test_Test3_shifterLeft():
    assert own.shifterLeft("",0) == "","test failed" 

def test_Test1_decrypt():
    assert own.decrypt("e742e6cf68a158") == "testing","test failed" 
def test_Test2_decrypt():
    assert own.decrypt("Dwadwadwdq2301392031zz2") == "Input tidak valid","test failed" 

def test_Test1_encrypt():
    assert own.encrypt(b"testing") == "e742e6cf68a158","test failed" 
def test_Test2_encrypt():
    assert own.encrypt(213123123) == "Input tidak valid","test failed" 


# def BytesToBits():
# def BitsToBytes():
# def xorBits():
# def shifterRight():
# def shifterLeft():
# def encrypt():
# def decrypt():

