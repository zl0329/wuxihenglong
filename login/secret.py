from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

# 密钥和偏移量
secret = '[geoin-building]'
iv = '[geoin-building]'

# AES CBC模式解密
password = 'HLadmin'
# 转换密码格式
data = pad(password)
# 字符串补位
aes = AES.new(secret.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
text = aes.encrypt(data.encode('utf-8'))
# 加密后得到的是bytes类型的数据，使用Base64进行编码，返回byte字符串
encodestr = base64.b64encode(text)
# 对byte字符串按utf8进行解码
pwd = encodestr.decode('utf8')
print("密文：", pwd)

# AES CBC模式加密
data = pwd.encode('utf8')
encodebyte = base64.decodebytes(data)
# 将加密数据转换为bytes类型数据
aes = AES.new(secret.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
text = aes.decrypt(encodebyte)
# 去补位
password = unpad(text)
password1 = password.decode('utf8')
print("明文：", password1)

# iv = '[geoin-building]'
#
# def AES_Encrypt(key, data):
#     data = pad(data)
#     cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
#     encryptedbytes = cipher.encrypt(data.encode('utf8'))
#     encodestrs = base64.b64encode(encryptedbytes)
#     enctext = encodestrs.decode('utf8')
#     return enctext

# if __name__ == '__main__':
#     secret = '[geoin-building]'
#     password = 'HLadmin'
#     en = AES_Encrypt(secret, password)
#     print(en)
