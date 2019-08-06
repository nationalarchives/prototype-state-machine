aws s3 cp s3://tdr-files/$FILE_NAME .
STATUS=`clamscan | head -n 1 | awk -F': ' '{print $2}'`
VIRUS_FOUND=false
if [[ $STATUS != "OK" ]]; then
    VIRUS_FOUND=true
fi
JSON=`jq -n --arg filename "$FILE_NAME" --arg status "$STATUS" --arg virusFound "$VIRUS_FOUND" '{filename: $filename, status: $status, virusFound: $virusFound}'`
echo "$JSON"
aws stepfunctions send-task-success --task-token $TASK_TOKEN_ENV_VARIABLE --task-output "$JSON"

