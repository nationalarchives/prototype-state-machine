docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD

docker push nationalarchives/tdr-checksum-check

docker push nationalarchives/tdr-virus-check

docker push nationalarchives/tdr-file-format-check
