#https://blog.csdn.net/Future_Hk/article/details/149615313?spm=1001.2014.3001.5501
#该脚本用于破解THM Order挑战的XOR信息

ciphertext = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
ciphertext += "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
ciphertext = bytes.fromhex(ciphertext) # 将十六进制字符串转换为字节序列


header = "ORDER:" # 已知的明文开头



key = ""
for i, c in enumerate(header):
    key += chr(ord(c) ^ ciphertext[i]) # 通过明文和密文异或得到密钥

print("Key:", key)


message = ""
for i, c in enumerate(ciphertext):
    message += chr(c ^ ord(key[i % len(key)])) # 使用密钥循环解密整个密文

print("Message:", message)
