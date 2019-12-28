def delete(key, secret, kw=[]):
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/delete"
    data = {"api_key" : key, "api_secret" : secret}
    data.update(kw)
    response = requests.post(http_url,data = data)

    req_dic = json.loads(response.text)
    print("Delete FaceSet:",req_dic)
    return req_dic

import json
import requests

key ="你的 API Key"
secret ="你的 API Secret"

kw = {'display_name':'demo' , 'outer_id':1 , 'tags':'person'}
delete(key, secret, kw)


