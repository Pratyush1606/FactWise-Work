import requests
import json


def get_token(user_id=1):
    # for getting tokens
    base_url = "http://127.0.0.1:8000/api/token/"
    endpoint = ""
    abs_url = base_url+endpoint

    data = {
        "username": "Matt",
        "password": "123456"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(abs_url, json.dumps(data), headers=headers)
    # print(response.status_code)
    # print(response.text)
    if(response.status_code==200):
        return response.json()["access"]

def post_user_permission(user_id=1, entity_id=1):
    base_url = "http://127.0.0.1:8000/enterprise"
    endpoint = "/user_permission/"+str(entity_id)


    abs_url = base_url+endpoint

    user_permissions = [
         {
            "action_api_group": "buyer_event",
            "entity_id": 1
         },
        {   
           "entity_id": 1,
           "action_api_group" : "buyer_event_creation" 
        },
        {   
           "entity_id": 1,
           "action_api_group" : "buyer_event_management" 
        },
        {   
           "entity_id": 1,
           "action_api_group" : "buyer_event_admin" 
        }
    ]
    access_token = get_token(1)
    headers = {
        "Content-Type": "application/json",
        'Authorization': 'Bearer '+str(access_token)
    }
    for user_permission in user_permissions:
        response = requests.post(abs_url, json.dumps(user_permission), headers=headers)
        print(response.status_code)

post_user_permission(1, 1)
# get_token(1)