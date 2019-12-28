def create(key, secret, kw=[]):  #建立人臉集合
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"
    data = {"api_key" : key, "api_secret" : secret}
    data.update(kw)
    response = requests.post(http_url,data = data)
    req_dic = json.loads(response.text)
    print("Create FaceSet:",req_dic)
    return req_dic

import json
import requests

key ="你的 API Key"
secret ="你的 API Secret"
kw = {'display_name':'login' , 'outer_id':1 , 'tags':'login'}  #人臉集合參數
create(key, secret, kw)

