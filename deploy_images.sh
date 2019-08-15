docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD

docker push nationalarchives/tdr-checksum-check:$1

docker push nationalarchives/tdr-virus-check:$1

docker push nationalarchives/tdr-file-format-check:$1
