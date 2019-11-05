container-structure-test test --image nationalarchives/tdr-virus-check:dev --config virus/config.yml
container-structure-test test --image nationalarchives/tdr-checksum-check:dev  --config checksum/config.yml
container-structure-test test --image nationalarchives/tdr-file-format-check:dev --config fileformat/config.yml
