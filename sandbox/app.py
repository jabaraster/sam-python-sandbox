import json
import cv2
import numpy as np
import boto3
import tempfile
import images


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    s3Event = event["Records"][0]["s3"]
    s3 = boto3.resource('s3')
    obj = s3.Bucket(s3Event['bucket']['name']).Object(s3Event['object']['key'])

    with tempfile.NamedTemporaryFile("wb") as f:
        obj.download_fileobj(f)
        img = cv2.imread(f.name)
        s = images.sum_color(img)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "color-summary": int(s)
            }),
        }