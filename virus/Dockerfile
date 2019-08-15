FROM ubuntu
RUN apt-get update \
            && apt-get install -y clamav python3-pip jq \
            && freshclam \
            && pip3 install awscli
COPY virus-check.sh /
WORKDIR /viruscheck
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION
ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
CMD bash /virus-check.sh
