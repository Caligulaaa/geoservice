import requests
import json


def auth():

    url_get_token = 'http://127.0.0.1:8000/api/v1/token/'
    data = {
        'username':'bandit',
        'password':'123',
    }
    response = requests.post(url_get_token,data=data)
    decode_response = json.loads(response.content)
    return decode_response['access']

def register(url):
    
    data = {
        'username':'cory',
        'password':'YaBandit17', 
        'password2': 'YaBandit17', 
        'email':'asasdasdd@gmail.com'
    }
    response = requests.post(url,data=data)
    decode_response = json.loads(response.content)
    return decode_response

def getWithoutAuth(url):
    response = requests.get(url)
    decode_response = json.loads(response.content)
    return decode_response


def postWithAuth(url):
    
    headers = {
        # "Accept": "application/json",
        'Authorization': f'AUTHTOKEN {auth()}',
        # 'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'name':'bandit',
    }
    response = requests.post(url,headers=headers,data=data)
    # response = requests.get(url,headers=headers)
    print(headers)
    decode_response = json.loads(response.content)
    return decode_response

def postWithoutAuth(url):
    
    data = {
        'name':'1',
    }
    response = requests.post(url,data=data)
    decode_response = json.loads(response.content)
    return decode_response

def deleteTest(url):
    headers = {
        # "Accept": "application/json",
        'Authorization': f'AUTHTOKEN {auth()}',
        # 'Content-Type': 'application/x-www-form-urlencoded',
    }    

    response = requests.delete(url,headers=headers)
    # response = requests.get(url)
    decode_response = json.loads(response.content)
    return decode_response


url = 'http://127.0.0.1:8000/api/wheel/comb/'
url1 = 'http://127.0.0.1:8000/api/wheel/addbox/'
url2 = 'http://127.0.0.1:8000/api/wheel/usersbox/1'

info_all_box = 'api/wheel/combackbox/'  # info about box for everybody
random_items = 'api/wheel/comb/' # take items only register and limit freespin   data:name
take_freespin = 'api/wheel/addbox/' # take freespin only register users
info_and_del_bag = 'api/wheel/usersbox/1' # information about owners items with pk-user and clear all items users
take_token = 'api/auth/token/' # take token username and pass
registration = 'api/auth/register/' # register give 10 freespin afte register

urlpattern = 'http://127.0.0.1:8000/'

# print(postWithAuth(urlpattern+info_and_del_bag))
# print(deleteTest(url2))
# print(postWithAuth(urlpattern+random_items))
# print(deleteTest(url2))
# print(register(urlpattern+registration))
def postWithAuth1(url):
    
    headers = {
        # "Accept": "application/json",
        'Authorization': f'TOKEN {auth()}',
        # 'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.get(url,headers=headers)
    # response = requests.get(url,headers=headers)
    decode_response = json.loads(response.content)
    return decode_response
# print(auth())
print(postWithAuth1('http://localhost:8000/api/v1/mypage/groups/'))