FROM alpine
RUN apk update && apk add py-pip && pip install awscli
WORKDIR checksum
CMD aws s3 cp s3://tdr-upload-files-dev/$FILE_NAME . \
                    && echo "{\"file\": \"$FILE_NAME\", \"checksum\": \"$(sha256sum ./* | awk '{print $1}')\"}" > tmp \
                    && aws stepfunctions send-task-success --task-token $TASK_TOKEN_ENV_VARIABLE --task-output "$(cat tmp)"

