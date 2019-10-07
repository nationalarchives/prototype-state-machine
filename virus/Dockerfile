FROM ubuntu
RUN apt-get update \
            && apt-get install -y clamav python3-pip jq \
            && freshclam \
            && pip3 install awscli
COPY process_file.py /
WORKDIR /viruscheck
CMD aws s3 sync s3://tdr-upload-files-dev/$CONSIGNMENT_ID . &&  clamscan > out.log && python3 /process_file.py




