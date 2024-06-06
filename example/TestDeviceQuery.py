from tuya_iot import TuyaOpenAPI
import hmac
import hashlib
import time

# Tuya API credentials
ACCESS_ID = "7unwntarrxfhr85yhpae" # your_access_id
ACCESS_KEY = "fd8079773e434e69996b7b8b3104e705" # your_access_key
API_ENDPOINT = "https://openapi.tuyaeu.com"

# Device ID of your sensor
DEVICE_ID = "bfc2b3fa45153c2207wttw" # your_device_id

# Initialize the Tuya OpenAPI object
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)

# Function to generate the current timestamp in milliseconds
def current_timestamp():
    return str(int(time.time() * 1000))

# Function to get the access token
def get_access_token():
    timestamp = current_timestamp()
    string_to_sign = ACCESS_ID + timestamp
    sign = hmac.new(
        bytes(ACCESS_KEY, 'utf-8'),
        msg=bytes(string_to_sign, 'utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest().upper()
    headers = {
        'client_id': ACCESS_ID,
        'sign': sign,
        't': timestamp,
        'sign_method': 'HMAC-SHA256',
        'Content-Type': 'application/json'
    }
    response = openapi.get('/v1.0/token?grant_type=1', headers=headers)
    if response['success']:
        return response['result']['access_token']
    else:
        print(f"Failed to get access token: {response}")
        return None

# Get the access token
access_token = get_access_token()

# Function to get the device status
def get_device_status():
    if access_token:
        url = f'/v1.0/iot-03/devices/{DEVICE_ID}/status'
        #url = f'/v1.0/devices/{DEVICE_ID}/status'
        headers = {
            'access_token': access_token,
            'client_id': ACCESS_ID,
            'sign_method': 'HMAC-SHA256',
            't': current_timestamp()
        }
        response = openapi.get(url, headers=headers)
        if response['success']:
            return response['result']
        else:
            print(f"Failed to get device status: {response}")
            return None
    else:
        print("Access token is not available.")
        return None

# Fetch the device status and print it
device_status = get_device_status()
if device_status:
    for status in device_status:
        print(f"Code: {status['code']}, Value: {status['value']}")
