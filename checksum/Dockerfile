FROM alpine
RUN apk update && apk add py-pip && pip install awscli
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION
ARG S3_UPLOAD_BUCKET
ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
ENV S3_UPLOAD_BUCKET $S3_UPLOAD_BUCKET
WORKDIR checksum
CMD aws s3 cp s3://$S3_UPLOAD_BUCKET/$FILE_NAME . \
                    && echo "{\"file\": \"$FILE_NAME\", \"checksum\": \"$(sha256sum ./* | awk '{print $1}')\"}" > tmp \
                    && aws stepfunctions send-task-success --task-token $TASK_TOKEN_ENV_VARIABLE --task-output "$(cat tmp)"

