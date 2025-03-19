# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re
import random

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM') or 120)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    'RK': 'oxEY1bTnXf',
    'ptcz': '53e3b35a9486dd63c4d06430b05aa169402117fc407dc5cc9329b41e59f62e2b',
    'pac_uid': '0_e63870bcecc18',
    'iip': '0',
    '_qimei_uuid42': '183070d3135100ee797b08bc922054dc3062834291',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FeEOpSbFh2Mb1bUxMW9Y3FRPfXwWvOLaNlsjWIkcKeeNg6vlVS5kOVuhNKGQ1M8zaggLqMPmpE5qIUdqEXlQgYg%2F132',
    'wr_gender': '0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=1ff5a0725f8841088b42f97109c45862',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}


"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
# 指定列表
b_values = [
    "32c322d072aadd6432c59a9",
    "4be320905b94534becfd24b",
    "d2c324d0723f69d6d2c98ec",
    "0ca32480813ab749cg016f04",
    "de1326c0813ab9641g0144d7",
    "5b532b1071d8ceb95b5cdeb",
    "bd8323b0715d9698bd82831",
    "8b9329607186dc198b9bdab",
    "50c32b70813ab8d2fg014d8a",
    "659320e0813ab990eg01339d",
    "390325d072479672390034f",
    "63432f80813ab7c0eg015a06",
    "54c32470813ab9779g019d78",
    "ef432b305dd664ef447bcb5",
    "0143250071c626730142037",
    "cf232ac057cbd8cf2cf9e99",
    "68c32bf05e22aa68c605298",
    "e47324d0813ab7f19g01610b",
    "2f632bd0813ab7d8eg014a5c",
    "c93329a071bfa32ec932b80",
    "d2332d80813ab8fe7g019c72",
    "898323405b7c438982e9e69",
    "ed732140813ab9bf0g010fe9",
    "d09327f0813ab952cg013009",
    "4fc32a70813ab9c31g01395d",
    "ba432ac0718b66b3ba4a6a0",
    "bb432f60813ab8444g014d61",
    "ef932da0813ab900ag0112eb",
    "705328d0813ab937eg016977",
    "22832f60813ab9c31g017302",
    "991320b0813ab7d6eg01136e",
    "c7c326c0813ab8f61g011550",
    "930323b072ae21a89302d43",
    "f90320d0813ab9c1cg015c54",
    "3f4320005d0ff13f440f223",
    "1f4326e0813ab7e0fg0167ca",
    "2cf32980813ab926bg01459b",
    "37432510729e9b5e3743e43",
    "44132240813ab7bbeg01417c",
    "35132df05e3a9235192ce0b",
    "44c32630813ab9467g0154e0",
    "73032d20813ab73aag0107dc",
    "92932780727b2999929fce4",
    "4b232040813ab9b48g014b40",
    "f7232eb0726c88e7f728da6",
    "bec32e207213d429bec5ec4",
    "29b3216072aadd6729b5fd4",
    "f0e32e20813ab8732g017411",
    "86932080813ab8b4cg01202f",
    "38532c70813ab7176g0142b5",
    "ca8327d0813ab8258g010615",
    "05e32e70813ab99fag0130ba",
    "10c32680813ab6eedg012be4",
    "f5d32560813ab7dbdg017fff",
    "39e323e0716a308739e70be",
    "5b932bd05cf3215b92b7cd5",
    "96632200813ab94f8g016077",
    "631324c0813ab735bg01382c",
    "95b32650724d5f3f95b80b6",
]

random_b_value = random.choice(b_values)
data = {
    "appId": "wb182564874663h152492176",
    "b": random_b_value,  # 从指定列表中随机选择
    "c": "7cb321502467cbbc409e62d",
    "ci": 70,
    "co": 0,
    "sm": "[插图]第三部广播纪元7年，程心艾AA说",
    "pr": 74,
    "rt": 30,
    "ts": 1727660516749,
    "rn": 31,
    "sg": "991118cc229871a5442993ecb08b5d2844d7f001dbad9a9bc7b2ecf73dc8db7e",
    "ct": 1727660516,
    "ps": "b1d32a307a4c3259g016b67",
    "pc": "080327b07a4c3259g018787",
}


def convert(curl_command):
    """提取bash接口中的headers与cookies
    支持 -H 'Cookie: xxx' 和 -b 'xxx' 两种方式的cookie提取
    """
    # 提取 headers
    headers_temp = {}
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers_temp[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    
    # 从 -H 'Cookie: xxx' 提取
    cookie_header = next((v for k, v in headers_temp.items() 
                         if k.lower() == 'cookie'), '')
    
    # 从 -b 'xxx' 提取
    cookie_b = re.search(r"-b '([^']+)'", curl_command)
    cookie_string = cookie_b.group(1) if cookie_b else cookie_header
    
    # 解析 cookie 字符串
    if cookie_string:
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key.strip()] = value.strip()
    
    # 移除 headers 中的 Cookie/cookie
    headers = {k: v for k, v in headers_temp.items() 
              if k.lower() != 'cookie'}

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
