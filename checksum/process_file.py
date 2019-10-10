import sys
import hashlib
import os
import json

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

sha256 = hashlib.sha256()

with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        sha256.update(data)
print(json.dumps(json.dumps({"file": os.environ["CONSIGNMENT_ID"] + "/" + sys.argv[1][2:], "checksum":  sha256.hexdigest()})))
