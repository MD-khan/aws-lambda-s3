import json
import urllib.parse
import boto3

print('Loading function')

#s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    file = get_text_file()
    result = count_word(file)
    return result

def count_word(texts):
    result = {}
    texts = texts.split()
    for text in texts:
        result[text] = 1
    else:
        result[text] += 1
        return result

def get_text_file():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('demo-s3-event-md')
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
    return body
