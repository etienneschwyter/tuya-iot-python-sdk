import time
import hmac
import hashlib
import requests

# Tuya API credentials
ACCESS_ID = "7unwntarrxfhr85yhpae" # your_access_id
ACCESS_KEY = "fd8079773e434e69996b7b8b3104e705" # your_access_key
API_ENDPOINT = "https://openapi.tuyaeu.com"

# Device ID of your sensor
DEVICE_ID = "bfc2b3fa45153c2207wttw" # your_device_id

def current_timestamp():
    return str(int(time.time() * 1000))

def get_signature(client_id, access_key, timestamp, access_token=None):
#    string_to_sign = f"{client_id}{timestamp}"
#    sign = hmac.new(
#        bytes(access_key, 'utf-8'),
#        msg=bytes(string_to_sign, 'utf-8'),
#        digestmod=hashlib.sha256
#    ).hexdigest().upper()
#    return sign
   # HTTPMethod
    str_to_sign = "GET\n"

    # Content-SHA256
    content_to_sha256 = ("")

    str_to_sign += (
        hashlib.sha256(content_to_sha256.encode(
            "utf8")).hexdigest().lower()
    )
    str_to_sign += "\n\n"

    # URL
    url = f"{API_ENDPOINT}/v1.0/devices/{DEVICE_ID}/status"
    str_to_sign += url

    # Sign
    t = current_timestamp()

    message = client_id
    if access_token is not None:
        message += access_token
    message += t + str_to_sign
    print(message)
    sign = (hmac.new(ACCESS_KEY.encode("utf8"), msg=message.encode("utf8"), digestmod=hashlib.sha256,).hexdigest().upper())
    
    return sign


def get_access_token(client_id, access_key):
    timestamp = current_timestamp()
    sign = get_signature(client_id, access_key, timestamp)
    
    headers = {
        'client_id': client_id,
        'sign': sign,
        't': timestamp,
        'sign_method': 'HMAC-SHA256',
        'Content-Type': 'application/json'
    }
    
    url = f"{API_ENDPOINT}/v1.0/token?grant_type=1"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('success'):
            return response_data['result']['access_token']
        else:
            print(f"Failed to get access token: {response_data}")
            return None
    else:
        print(f"HTTP Error: {response.status_code}")
        return None

def get_device_status(client_id, access_key, device_id, access_token):
    timestamp = current_timestamp()
    sign = get_signature(client_id, access_key, timestamp, access_token)
    
    headers = {
        'client_id': client_id,
        'sign': sign,
        't': timestamp,
        'sign_method': 'HMAC-SHA256',
        'Content-Type': 'application/json',
        'access_token': access_token
    }
    
    url = f"{API_ENDPOINT}/v1.0/devices/{device_id}/status"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('success'):
            return response_data['result']
        else:
            print(f"Failed to get device status: {response_data}")
            return None
    else:
        print(f"HTTP Error: {response.status_code}")
        return None

# Get the access token
access_token = get_access_token(ACCESS_ID, ACCESS_KEY)

# Fetch the device status and print it
if access_token:
    device_status = get_device_status(ACCESS_ID, ACCESS_KEY, DEVICE_ID, access_token)
    if device_status:
        for status in device_status:
            print(f"Code: {status['code']}, Value: {status['value']}")
else:
    print("Access token is not available.")
