import requests
import json

def sendsms(number,message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params={
        "authorization":'JDSGNPFlesuLtWqp5TxwyEXZIj410Y79cnfiBdQKmag6ARzOVkFTxn6r1HBGzehPEKRtI5vkp4gOsZay',
        "sender_id":'FSTSMS',
        "message":message,
        "language":'english',
        "route":'v3',
        "numbers":number
    }
    response=requests.get(url,params=params)
    a=response.json()
    print(a)


sendsms("6232769986","hello Manvi here")
    


