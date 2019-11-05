container-structure-test test --image  nationalarchives/tdr-virus-check --config virus/config.yml
container-structure-test test --image nationalarchives/tdr-checksum-check  --config checksum/config.yml
container-structure-test test --image nationalarchives/tdr-file-format-check --config fileformat/config.yml
