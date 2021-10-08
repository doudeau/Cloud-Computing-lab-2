

import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://queue.amazonaws.com/976055184967/test'
while True :
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    try :
        message = response['Messages'][0]
        receipt_handle = response['ReceiptHandle']
        numbers = message['MessageAttributes']['Numbers']['StringValue']

        sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    except :
        continue

    print(numbers)

