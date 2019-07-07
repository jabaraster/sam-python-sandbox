sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket jabara-sam-packages \
&& sam deploy \
    --template-file packaged.yaml \
    --stack-name python-sam-sample \
    --capabilities CAPABILITY_IAM