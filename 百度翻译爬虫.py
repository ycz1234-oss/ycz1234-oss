import requests
import time
import random
from hashlib import md5


# 获取salt sign ts
def get_salt_sign_ts(word):
#     salt获取
    ts = str(int(time.time()*1000))
    salt = ts + str(random.randint(0,9))

    string = 'fanyideskweb'+word+salt+'n%A-rKaT5fb[Gy?N5@Tj'
    s=md5()
    s.update(string.encode())
    sign=s.hexdigest()

    return salt,ts,sign

# 破解有道
def attack_yd(word):
    salt,ts,sign = get_salt_sign_ts(word)
#     定义
    url = ''
  # headers和data是自己抓取，因为参考的比较久，反扒机制已经升级，这里就没写，过几天写个新的。
    headers={}
    data = {}
    html_json=requests.post(
        url=url,
        data=data,
        headers=headers,
    ).json()

    return html_json

if __name__ == '__main__':
    word = input('请输入要翻译的单词')
    result = attack_yd(word)
    print(result)
