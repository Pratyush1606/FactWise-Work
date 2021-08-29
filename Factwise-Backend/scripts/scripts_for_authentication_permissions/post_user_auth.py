import requests
import json

def post_user_auth(user_id=1):
    base_url = "http://127.0.0.1:8000/enterprise"
    endpoint = "/user_auth/"+str(user_id)


    abs_url = base_url+endpoint

    data = {
        "username": "Matt",
        "password": "123456"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(abs_url, json.dumps(data), headers=headers)
    print(response.status_code)
    print(response.text)

post_user_auth(1)