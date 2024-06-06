import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

# Tuya API credentials
ACCESS_ID = "7unwntarrxfhr85yhpae" # your_access_id
ACCESS_KEY = "fd8079773e434e69996b7b8b3104e705" # your_access_key
API_ENDPOINT = "https://openapi.tuyaeu.com"

# Device ID of your sensor
DEVICE_ID = "bfc2b3fa45153c2207wttw" # your_device_id

# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Call APIs from Tuya

# Get the status of a single device
response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))