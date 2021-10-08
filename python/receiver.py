import boto3

# Create SQS client
sqs = boto3.client('sqs')
def create_queue():
    try :
        queue = sqs.get_queue_by_name(QueueName='responseQueue')
    except :
        queue = sqs.create_queue(QueueName='responseQueue', Attributes={'DelaySeconds': '5'})
    return queue

def receive(queue) :
    while True :
        # Receive message from SQS queue
        response = sqs.receive_message(
            QueueUrl=queue,
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
            QueueUrl=queue,
            ReceiptHandle=receipt_handle
            )

            print(numbers)
            return numbers
        except :
            print("attente")



def send(queue):
    response = queue.send_message(
        MessageBody='boto3', 
        MessageAttributes={
            'Numbers': {
                'StringValue': 'oui',
                'DataType': 'String'
                    }
    })

def main():
    queue = create_queue()
    receive('https://sqs.us-east-1.amazonaws.com/976055184967/requestQueue')
    send(queue)

main()