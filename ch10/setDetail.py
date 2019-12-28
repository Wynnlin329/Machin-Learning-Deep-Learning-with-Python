def detail(key, secret, outer_id):  #查看人臉集合內容
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail"
    data = {"api_key": key, "api_secret": secret, "outer_id": outer_id}
    response = requests.post(http_url, data=data)
    req_dic = json.loads(response.text)
    print("Faceset Detail:",req_dic)
    return req_dic

import json
import requests

key ="你的 API Key"
secret ="你的 API Secret"

detail(key, secret, 1)  #outer_id=1
