import subprocess
import json
import boto3
import os

def lambda_handler(event, context):
    

    s3 = boto3.client("s3")
    s3_object = s3.get_object(Bucket="tdr-files", Key="500standardsizefiles/003533e1-bfe1-44bc-82b6-a19902e7a346.jpg")
    with open('/tmp/main.cvd', 'wb') as data:
        s3.download_fileobj('tdr-files', 'main.cvd', data)
    streaming_body = s3_object["Body"]
    av_env = os.environ.copy()
    av_env["LD_LIBRARY_PATH"] = "./bin" 

    process = subprocess.Popen(['./bin/clamscan', '-d', '/tmp/main.cvd', '-'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE,
                     env=av_env)
    stdout, stderr = process.communicate(streaming_body)
    print(stdout)
    print(stderr)
    return json.dumps({"msg": stdout.decode("utf-8") })

