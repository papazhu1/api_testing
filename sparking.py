# -*- coding:utf-8 -*-
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import json
import requests

'''
1、文本改写 Web API 调用示例
2、运行前：请先填写Appid、APIKey、APISecret 相关信息
'''

class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg

class Url:
    def __init__(this, host, path, schema):
        this.host = host
        this.path = path
        this.schema = schema
        pass

class wsParam(object):
    def __init__(self):
        self.APPID = "3490ec98"
        self.APIKey = "21e4d6b505010629f83f689703355448"
        self.APISecret = "YmJjMDc1ZWMzMzMyOTRiMDhkYzgwOGFm"
        self.url = 'https://api.xf-yun.com/v1/private/se3acbe7f'
        self.level = level

    def parse_url(self,requset_url):
        stidx = requset_url.index("://")
        host = requset_url[stidx + 3:]
        schema = requset_url[:stidx + 3]
        edidx = host.index("/")
        if edidx <= 0:
            raise AssembleHeaderException("invalid request url:" + requset_url)
        path = host[edidx:]
        host = host[:edidx]
        u = Url(host, path, schema)
        return u

    def init_header(self):
        headers = {
            'content-type': "application/json",
            'host': 'api.xf-yun.com'
        }
        return headers

    def get_body(self):
        data = {
            "header": {
                "app_id": self.APPID,
                "status": 3,
            },
            "parameter": {
                "se3acbe7f": {
                    "level": self.level,
                    "result": {
                        "encoding": "utf8",
                        "compress": "raw",
                        "format": "json"
                    }
                }
            },
            "payload": {
                "input1": {
                    "encoding": "utf8",
                    "compress": "raw",
                    "format": "plain",
                    "status": 3,
                    "text": str(base64.b64encode(text.encode('utf-8')), 'utf-8')
                }
            }
        }
        body = json.dumps(data)
        return body

def assemble_ws_auth_url(requset_url, method="POST", api_key="", api_secret=""):
    u = wsParam.parse_url(requset_url)
    host = u.host
    path = u.path
    now = datetime.now()
    date = format_date_time(mktime(now.timetuple()))
    print(date)
    # date = "Thu, 12 Dec 2019 01:57:27 GMT"
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(host, date, method, path)
    print("----2",signature_origin)
    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin.encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
    authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        api_key, "hmac-sha256", "host date request-line", signature_sha)
    print("----1:",authorization_origin)
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
    print(authorization_origin)
    values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }
    return requset_url + "?" + urlencode(values)

def get_result():
    request_url = assemble_ws_auth_url(wsParam.url, "POST", wsParam.APIKey, wsParam.APISecret)
    print("request_url:", request_url)
    response = requests.post(request_url, data=wsParam.get_body(), headers=wsParam.init_header())
    print("response:", response)
    str_result = response.content.decode('utf8')
    json_result = json.loads(str_result)
    print("response-content:", json_result)
    if json_result. __contains__('header') and json_result['header']['code'] == 0:
        renew_text = json_result['payload']['result']['text']
        print("\n改写结果：", str(base64.b64decode(renew_text), 'utf-8'))
        #改写结果保存到文件
        #result_file = open(".\改写结果.txt",'w',encoding='utf-8')
        #result_file.write(str(base64.b64decode(renew_text), 'utf-8'))


if __name__ == "__main__":
    APPID = "3490ec98"
    APISecret = "21e4d6b505010629f83f689703355448"
    APIKey = "YmJjMDc1ZWMzMzMyOTRiMDhkYzgwOGFm"
    level = "<L3>" #改写等级 <L1>  ~  <L6>  等级越高，改写程度越深
    text = "青少年教育创意平台是指专为青少年设计的在线或线下环境，旨在提供创新和创造性学习体验的平台。这样的平台通常结合了教育技术和先进的教学方法，以激发年轻人的兴趣，培养他们的创造力、批判性思维和解决问题的能力。"
    # 上传文件
    #text = open(r"文本.txt",encoding='utf-8').read()
    wsParam = wsParam()
    get_result()
