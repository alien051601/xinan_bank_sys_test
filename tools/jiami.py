from Crypto.Cipher import AES
from binascii import b2a_base64, a2b_base64


class Prpcrypt(object):
    # 解密的秘钥
    key = b"c572ea1baopaw598"
    aes = AES.new(key, AES.MODE_ECB)
    text = str()
    def pad(self, text):
        while len(text) % 16!= 0:
            text += "\t"
        return text

    def jiami(self, text_16):
        pre_encry = text_16.encode()
        res = self.aes.encrypt(pre_encry)
        result = str(b2a_base64(res),encoding="utf-8")
        r = result.strip("\n")
        print("加密之后的密文：",r,"密码长度为：",len(r))
        return r

    def decrypt(self, text_16):
        pre_decry = text_16.encode()
        texts = a2b_base64(pre_decry)
        res = str(self.aes.decrypt(texts), encoding="utf8")
        n = res.strip("\t")
        print("解密之后的明文：",n, "明文长度为：",len(n))
        return n



# if __name__ == "__main__":
#     p = Prpcrypt()
#     pw = "a123456"
#     pw_b = p.pad(pw)
#     jiami = p.jiami(pw_b)
#
#     res = p.decrypt(jiami)


    # jiemi = "C3pwf3Cz/0Ofk/QV7CHWvA=="
    # p.decrypt(jiemi)