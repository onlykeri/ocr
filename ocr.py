import time
import urllib
import json
import hashlib
import base64
from urllib import parse,request

def fun(filepath):#讯飞科大的API
    f = open(filepath, 'rb')#图片存放位置
    file_content = f.read()
    base64_image = base64.b64encode(file_content)
    body = urllib.parse.urlencode({'image': base64_image})  # body数据
    body = bytes(body, 'utf-8')
    url = 'http://webapi.xfyun.cn/v1/service/v1/ocr/handwriting'
    api_key = 'this_is_apiKey'#申请的apiKey
    param = {"language":"en", "location":"false"}  # header中参数
    param_json = json.dumps(param).replace(' ', '')#字符串类型
    x_appid = 'you_APIID'#讯飞的APIID，自己申请的
    param1=bytes(param_json,'utf-8')
    #pdb.set_trace()
    x_param = base64.b64encode(param1)
    x_param_decode = x_param.decode('utf-8')
    x_time = int(int(round(time.time() * 1000)) / 1000)
    text = api_key + str(x_time) + x_param_decode
    text = bytes(text, 'utf-8')
    x_checksum = hashlib.md5(text).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read().decode("utf-8")
    print(":" + result)
    file = open('./all.txt','a',encoding = 'utf-8')
    file.write(result)
    file.close()
    return result

def main():
	for i in range(1,33):
		r = str(i)
		url1 = str("./image/title" + r + ".png") # 识别image文件夹下的第r张图片
		str_data = str(url1)
		fun(str_data)


if __name__ == '__main__':
    main()