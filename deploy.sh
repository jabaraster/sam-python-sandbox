sam build \
&& sam package \
    --template-file ./.aws-sam/build/template.yaml \
    --output-template-file ./.aws-sam/build/packaged.yaml \
    --s3-bucket jabara-sam-packages \
&& sam deploy \
    --template-file ./.aws-sam/build/packaged.yaml \
    --stack-name python-sam-sample \
    --capabilities CAPABILITY_IAM