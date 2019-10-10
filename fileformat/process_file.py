import sys
import subprocess

res = subprocess.check_output(["sf", "-json",sys.argv[1][2:]])
for line in res.splitlines():
    subprocess.call(["aws","sns","publish","--topic-arn","arn:aws:sns:eu-west-2:247222723249:fileformat-check-result-dev","--message",line])
