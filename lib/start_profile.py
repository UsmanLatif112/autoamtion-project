from lib.create_profile import create_profile
from lib.imports import *
from lib.data import *
from lib.function import *

"""=============================================================="""

        
"""=============================================================="""       
token = Mlx_data().get_access_token()
HEADERSS = {  
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }
FOLDER_ID = Mlx_data.folder_id
PROFILE_ID = None

"""=============================================================="""


def start_profile() -> webdriver:
    r = requests.get(
        f"https://launcher.mlx.yt:45001/api/v2/profile/f/725851d5-eac0-498b-9781-e1b358c69ff1/p/6e9a248c-6b74-4018-aeba-591aa8a2cd3c/start?automation_type=selenium",headers=HEADERSS,)
    response = r.json()
    if r.status_code != 200:
        print(f"\nError while starting profile: {r.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} started.\n")
        profile_iD = f'{PROFILE_ID}'
    selenium_port = response["data"]["port"]
    driver = webdriver.Remote(
        command_executor=f"http://127.0.0.1:{selenium_port}", options=ChromiumOptions()
    )
    return driver


# def start_profile() -> webdriver:
    
#     global PROFILE_ID
#     PROFILE_ID = create_profile()
#     r = requests.get(
#         f"https://launcher.mlx.yt:45001/api/v2/profile/f/{FOLDER_ID}/p/{PROFILE_ID}/start?automation_type=selenium",headers=HEADERSS,)
#     response = r.json()
#     if r.status_code != 200:
#         print(f"\nError while starting profile: {r.text}\n")
#     else:
#         print(f"\nProfile {PROFILE_ID} started.\n")
#         profile_iD = f'{PROFILE_ID}'
#     selenium_port = response["data"]["port"]
#     driver = webdriver.Remote(
#         command_executor=f"http://127.0.0.1:{selenium_port}", options=ChromiumOptions()
#     )
#     return driver,profile_iD


"""=============================================================="""


# def stop_profile():
#     url = f"https://launcher.mlx.yt:45001/api/v1/profile/stop/p/{PROFILE_ID}"
    
#     payload={}
#     headers = HEADERSS
#     response = requests.request("GET", url, headers=headers, data=payload)
#     if response.status_code != 200:
#         print(f"\nError while stopping profile: {response.text}\n")
#     else:
#         print(f"\nProfile {PROFILE_ID} stopped.\n")

def stop_profile():
    url = f"https://launcher.mlx.yt:45001/api/v1/profile/stop/p/6e9a248c-6b74-4018-aeba-591aa8a2cd3c"
    
    payload={}
    headers = HEADERSS
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"\nError while stopping profile: {response.text}\n")
    else:
        print(f"\nProfile 6e9a248c-6b74-4018-aeba-591aa8a2cd3c stopped.\n")
        
 
"""=============================================================="""              
        
def remove_profile():
    url = "https://api.multilogin.com/profile/remove"
    payload = json.dumps({
    "ids": [PROFILE_ID],
    "permanently": False
    })
    HEADERS = HEADERSS
    response = requests.request("POST", url, headers=HEADERS, data=payload)
    if response.status_code != 200:
        print(f"\nError while deleting profile: {response.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} Deleted.\n")
    
"""=============================================================="""   
 