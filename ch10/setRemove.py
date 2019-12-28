def remove(key, secret, faceset_token, face_tokens):  #移除人臉特徵
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface"
    data = {"api_key": key, "api_secret": secret, "faceset_token" : faceset_token, "face_tokens" : face_tokens}
    response = requests.post(http_url, data=data)
    req_dic = json.loads(response.text)
    print("Remove face:",req_dic)
    return req_dic

import json
import requests

key ="你的 API Key"
secret ="你的 API Secret"
faceset_token = '77f6b2b55de164aa0d33be482b57be5f'

remove(key, secret, faceset_token, '0b0d68e028481782ea05656559f08f9a')

