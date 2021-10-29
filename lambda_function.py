import json
import ssl
import os


foobar = ssl.get_default_verify_paths()
foobar = os.listdir(foobar.openssl_capath)

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': foobar
    }
