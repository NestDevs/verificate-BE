import os
import requests
from dotenv import load_dotenv
from src.utils.constants import PINATA_URL_PIN_FILE,PINATA_URL_GET_FILE
load_dotenv()
import json
import datetime

def convert_to_time(time_stamp):
    """
        Converts the time stamp to a readable format
        :param time_stamp:
        :return:
            readable time stamp(date and time)
    """
    new_time = datetime.datetime.strptime(time_stamp,"%Y-%m-%dT%H:%M:%S.%fZ")
    return new_time.strftime("%Y-%m-%d %H:%M:%S")


def upload_certificate_to_ipfs(file_path,file_name):
    """
        Uploads a file to IPFS and returns the hash
        :param file_path:
        :return:
            uploaded file hash
    """
    try:

        payload={'pinataOptions': '{"cidVersion": 1}',
        'pinataMetadata': '{"name": "MyFile", "keyvalues": {"company": "Pinata"}}'}
        files=[
        ('file',(file_name,open(file_path+"/"+file_name,'rb'),'application/octet-stream'))
        ]
        headers = {
        'Authorization': f'Bearer {os.getenv("PINATA_JWT")}'
        }

        response = requests.request("POST", PINATA_URL_PIN_FILE, headers=headers, data=payload, files=files)
        return json.dumps({
            "success":True,
            "hash":response.json()["IpfsHash"],
            "pinSize":f"{round(float(response.json()['PinSize'])/1024,3)} MB",
            "timeStamp":convert_to_time(response.json()["Timestamp"])
        })

    except Exception as error:
        res = json.dumps({
            "error": str(error),
            "success":False
            })
        return res


def get_certificate_from_ipfs(ipfs_hash):
    """
        Gets certificate from ipfs
        :param ipfs_hash:
        :return:
            certificate
    """
    return PINATA_URL_GET_FILE+"/"+ipfs_hash

