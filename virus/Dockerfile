FROM ubuntu
RUN apt-get update \
            && apt-get install -y clamav python3-pip jq \
            && freshclam \
            && pip3 install awscli
COPY virus-check.sh /
WORKDIR /viruscheck
CMD bash /virus-check.sh




