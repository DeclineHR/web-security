# https://blog.csdn.net/Future_Hk/article/details/149668189?spm=1001.2014.3001.5501

ciphertext = "3019380d23553019182721290137271065161d30253f074532081d0c1e0616250c462616293a042e"
ciphertext = bytes.fromhex(ciphertext) # 将十六进制字符串转换为字节序列
a = 32
while(a < 128):
    flag = ""
    key = "dQuv" # 已知的key
    key += chr(a) #通过遍历chr(32-127) 即所有的常见字符来爆破
    a += 1
    for i, c in enumerate(ciphertext):
        flag += chr(c ^ ord(key[i % len(key)])) # XOR解密
        if(flag[len(flag)-1]== '}'):
                print("flag:", flag)
                print("key:", key)
                break
