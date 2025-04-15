# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re
import random

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认40次/20分钟
READ_NUM = int(os.getenv('READ_NUM') or 40)
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


# 书籍
book = [
"5c53218071c437db5c5121d",
"c6b32d50813ab96c6g012362",
"5b932bd05cf3215b92b7cd5",
"1f4326e0813ab7e0fg0167ca",
"68c32bf05e22aa68c605298",
"ce5321f071541ebfce59713",
"bd8323b0715d9698bd82831",
"d2332d80813ab8fe7g019c72",
"ef932da0813ab900ag0112eb",
"f0e32e20813ab8732g017411",
"61832e20813ab6d31g0140a7",
"c7c326c0813ab8f61g011550",
"2ce329305b1dca2ceb95926",
"8333202058318c833b4a523",
"495326205de23a49561a05d",
"716320805d2344716703998",
"cf232ac057cbd8cf2cf9e99",
"2f632bd0813ab7d8eg014a5c",
"86e32de0813ab9348g0128f5",
"35d32790813ab9a7cg01454c",
"b0b32130813ab9c34g016c1e",
"64c32e10813ab6e7ag0176cc",
"ca8327d0813ab8258g010615",
"38532c70813ab7176g0142b5",
"0bc32db0574fc00bc053afc",
"bbe32070813ab9a6ag011bc1",
"3f4320005d0ff13f440f223",
"f5d32560813ab7dbdg017fff",
"3a832f705d0d1f3a8ec72ff",
"5b532b1071d8ceb95b5cdeb",
"10c32680813ab6eedg012be4",
"35132df05e3a9235192ce0b",
"22732860813ab865ag012262",
"53b324f0813ab9389g019959",
"d5632fc0813ab6e28g014ccc",
"ba432ac0718b66b3ba4a6a0",
"0143250071c626730142037",
"05e32e70813ab99fag0130ba",
"4be320905b94534becfd24b",
"c75326607268db88c7582ab",
"703325005d2088703a3a142",
"37432510729e9b5e3743e43",
"be732b507248f2b8be78bb7",
"9a332f70813ab80efg0123b7",
"92932780727b2999929fce4",
"ece32ff0813ab8edag010f9a",
"e0c32c90813ab9859g012683",
"c5b32c00813ab9752g01957a",
"898323405b7c438982e9e69",
"64732850813ab935fg0158fb",
"d2c324d0723f69d6d2c98ec",
"d09327f0813ab952cg013009",
"2e032e407203c27a2e04de8",
"18532db07155b940185a03c",
"7e732d50813ab8508g0130ad",
"dfc32660720582eadfcb192",
"a0532580722fcef1a0518a1",
"4d032df0724b40164d0610e",
"68c32e00813ab9c5eg017621",
"91a322807186dc1d91a8646",
"edc32ee0718f987cedc2ad8",
"a6c32000813ab6c04g013ced",
"16832420813ab90f3g019f92",
"3c632a40723f428b3c6e85b",
"79632da0813ab9bb7g010002",
"8f532bd07278850c8f51770",
"86932080813ab8b4cg01202f",
"2a6329005e39922a6a6becc",
"5713236071a0f62957176e6",
"c9532130813ab95d0g0142f8",
"bb432f60813ab8444g014d61",
"e7332390813ab6c64g011712",
"89732a7072b44a0c8970477",
"57432c70813ab8b4bg013d9f",
"fa5323907289382afa599ff",
"744328a0813ab9c69g019aeb",
"ed432040813ab7ee9g014d4a",
"ff6323605ceabbff6f4f04e",
"94f32c30813ab9942g0158fd",
"95b32650724d5f3f95b80b6",
"9aa324a0813ab93fbg012922",
"2cf32980813ab926bg01459b",
"39e323e0716a308739e70be",
"4b232040813ab9b48g014b40",
"45132540813ab9b55g0183ed",
"00f326c0813ab962dg012a16",
"91c32f20813ab91e9g016a8c",
"bcb32150719afe3bbcbad52",
"e47324d0813ab7f19g01610b",
"c93329a071bfa32ec932b80",
"ed732140813ab9bf0g010fe9",
"0fe32f10728dd59e0fe60bf",
"64532550813ab9ae1g0122c5",
"4fc32a70813ab9c31g01395d",
"df932360813ab9c1bg017c0f",
"ef432b305dd664ef447bcb5",
"47e32d60813ab6faeg01919d",
"99032c20813ab8158g0160cf",
"819321e0813ab880ag01960c",
"a8732a00813ab953eg011dd0",
"705328d0813ab937eg016977",
"378327d05e27f7378ab1ea4",
"09832420813ab9ba1g011e20",
"22832f60813ab9c31g017302",
"991320b0813ab7d6eg01136e",
"63432f80813ab7c0eg015a06",
"930323b072ae21a89302d43",
"54c32470813ab9779g019d78",
"57a325d0813ab8481g0182bc",
"f90320d0813ab9c1cg015c54",
"6a732ce07201202c6a7b30a",
"57e324b05d047c57ebe463e",
"f86327607273bcfef869430",
"5c6323a05ddc1c5c6572bd3",
"824324f071d5681782467d4",
"70b32540813ab85e4g018268",
"390325d072479672390034f",
"50c32b70813ab8d2fg014d8a",
"060328405e27e2060260e81",
"4f532f205e27ea4f50c9a75",
"2f6327c0595a6a2f6db663f",
"1f5322605bfe8f1f5105803",
"0ca32480813ab749cg016f04",
"8703208072770583870a6fc",
"7f0327d0813ab7edag018663",
"44132240813ab7bbeg01417c",
"974320a0813ab92c1g0144f0",
"e9a321b0813ab95eeg012af7",
"32c322d072aadd6432c59a9",
"8ce32f007188b3668ce4238",
"121323f0729ac578121ce6f",
"44c32630813ab9467g0154e0",
"8b9329607186dc198b9bdab",
"73032d20813ab73aag0107dc",
"7c632ef05a49197c62b53f0",
"ea2326f071935f5fea206f1",
"de1326c0813ab9641g0144d7",
"f7232eb0726c88e7f728da6",
"6a732f3071645e9b6a72a2b",
"cb5321c071c9e1a3cb5a951",
"9b532db071a0ff999b5a465",
"bec32e207213d429bec5ec4",
"29b3216072aadd6729b5fd4",
"8ab32b9071a0f5418abd0c8",
"c4732cd072706ebfc472c34",
"96632200813ab94f8g016077",
"74032d80716395ce740fbf4",
"d1732010813ab983cg012120",
"33d32b0071ffa30233d0e03",
"ff032ea071e06ef4ff0f844",
"aad321e07268789aaade032",
"4f7320f0717f541a4f7ae8e",
"f7632f50813ab9598g01376d",
"9df32a605cda369dfe9964b",
"4bf326d0813ab817bg011ee0",
"c653236071e55adbc6552fe",
"129322d0813ab7107g013e14",
"445321305ce95a445011c90",
"f1e32af0719ecf67f1e2cba",
"7e832c10813ab6dccg01894b",
"659320e0813ab990eg01339d",
"3e132f70716c545f3e1c0d4",
"87d32d00715af12587d0237",
"fc9320b05c0ffdfc9b90cc3",
"9e3326b0813ab9231g012def",
"139329c05b6f7713924e08a",
"631324c0813ab735bg01382c",
"824324107235e5778248092",
]

# 章节
chapter = [
    "ecc32f3013eccbc87e4b62e","a87322c014a87ff679a21ea","e4d32d5015e4da3b7fbb1fa","16732dc0161679091c5aeb1",
    "8f132430178f14e45fce0f7","c9f326d018c9f0f895fb5e4","45c322601945c48cce2e120","d3d322001ad3d9446802347",
    "65132ca01b6512bd43d90e3","c20321001cc20ad4d76f5ae","c51323901dc51ce410c121b","aab325601eaab3238922e53",
    "9bf32f301f9bf31c7ff0a60","c7432af0210c74d97b01b1c","70e32fb021170efdf2eca12","6f4322302126f4922f45dec"
]

"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    "appId": "wb182564874603h266381671",
    "b": random.choice(book),
    "c": "7f632b502707f6ffaa6bf2e",
    "ci": 27,
    "co": 389,
    "sm": "19聚会《三体》网友的聚会地点是一处僻静",
    "pr": 74,
    "rt": 15,
    "ts": 1744264311434,
    "rn": 466,
    "sg": "2b2ec618394b99deea35104168b86381da9f8946d4bc234e062fa320155409fb",
    "ct": 1744264311,
    "ps": "4ee326507a65a465g015fae",
    "pc": "aab32e207a65a466g010615",
    "s": "36cc0815"
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
