FROM ubuntu
RUN apt-get update \
                && apt-get install -y wget gnupg2 python3-pip \
                && wget -qO - https://bintray.com/user/downloadSubjectPublicKey?username=bintray | apt-key add - \
                && echo "deb http://dl.bintray.com/siegfried/debian wheezy main" | tee -a /etc/apt/sources.list \
                && apt-get update \
                && apt-get install -y siegfried \
                && pip3 install awscli
WORKDIR fileformat
CMD aws s3 cp s3://tdr-upload-files-dev/$FILE_NAME . \
                && sf -json . > tmp \
                && aws stepfunctions send-task-success --task-token $TASK_TOKEN_ENV_VARIABLE --task-output "$(cat tmp)"


