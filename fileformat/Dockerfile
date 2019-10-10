FROM ubuntu
RUN apt-get update \
                && apt-get install -y wget gnupg2 python3-pip \
                && wget -qO - https://bintray.com/user/downloadSubjectPublicKey?username=bintray | apt-key add - \
                && echo "deb http://dl.bintray.com/siegfried/debian wheezy main" | tee -a /etc/apt/sources.list \
                && apt-get update \
                && apt-get install -y siegfried \
                && pip3 install awscli
WORKDIR fileformat
COPY process_file.py /
CMD aws s3 sync s3://tdr-upload-files-dev/$CONSIGNMENT_ID . && \
				find . -type f -exec python3 /process_file.py {} \;


