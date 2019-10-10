FROM alpine
COPY process_file.py /
RUN apk update && apk add py-pip && pip install awscli
WORKDIR checksum
CMD aws s3 sync s3://tdr-upload-files-dev/$CONSIGNMENT_ID . && find . -type f -exec python /process_file.py {} \; | xargs -I % sh -c 'aws sns publish --topic-arn arn:aws:sns:eu-west-2:247222723249:checksum-check-result-dev --message %';
