container-structure-test test --image nationalarchives/tdr-virus-check:latest --config virus/config.yml
container-structure-test test --image nationalarchives/tdr-checksum-check:latest --config checksum/config.yml
container-structure-test test --image nationalarchives/tdr-file-format-check:latest --config fileformat/config.yml