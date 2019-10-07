import os
import json
import subprocess

with open('out.log') as reader:
    for line in reader.readlines():
        if "/viruscheck" in line:
            parts = line.split(":")
            file_path = str(os.environ['CONSIGNMENT_ID']) + parts[0][11:]
            result = {"status": parts[1].strip(), "filename": file_path}
            subprocess.call(["aws","sns","publish","--topic-arn","arn:aws:sns:eu-west-2:247222723249:virus-check-result-dev","--message",json.dumps(result)])
        
