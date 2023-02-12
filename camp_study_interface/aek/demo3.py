from Crypto.Cipher import AES
import base64


# 自己定义一段密钥 -- 1234567812345678
# 16位的一串字符 -- 随便你定义 -- 让它和服务端用的是同一个东西

class EncryptDate:
    def __init__(self, key):
        self.key = key.encode("utf-8")  # 初始化密钥
        self.length = AES.block_size
        self.aes = AES.new(self.key, AES.MODE_ECB)
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text): #
        count = len(text.encode("utf-8"))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        # Base64是网络上最常见的用于传输8Bit字节码的编码方式之一
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


if __name__=='__main__':
    key = "1234567812345678"
    eg = EncryptDate(key)
    res = eg.encrypt("tony")
    pwd = eg.encrypt("123456")
    print(res)
    print(pwd)
    print("======接口端拿到了这段密文=======")
    print(eg.decrypt(res))
    print(eg.decrypt(pwd))