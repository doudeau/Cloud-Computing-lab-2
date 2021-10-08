import boto3

# Get the service resource
sqs = boto3.resource('sqs')

def create_queue():
    # Create the queue. This returns an SQS.Queue instance
    try :
        queue = sqs.get_queue_by_name(QueueName='requestQueue')
    except :
        queue = sqs.create_queue(QueueName='requestQueue', Attributes={'DelaySeconds': '5'})
    return queue
    

def send_numbers(numbers,queue) :

    response = queue.send_message(
        MessageBody='boto3', 
        MessageAttributes={
            'Numbers': {
                'StringValue': numbers,
                'DataType': 'String'
                    }
    })
    # You can now access identifiers and attributes
    #print(queue.url)

def receive():
    while True :
        try :
            queue = sqs.get_queue_by_name(QueueName='requestQueue')
        except:
            print("attente")

        try :
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
        except :
            print('ici')
        try :
            message = response['Messages'][0]
            receipt_handle = response['ReceiptHandle']
            res = message['MessageAttributes']['Numbers']['StringValue']

            sqs.delete_message(
            QueueUrl=queue,
            ReceiptHandle=receipt_handle
            )
            return res

        except Exception as e :
            print(e)

    

def main():
    queue = create_queue()
    send_numbers('2,5,6,3,8,9,4,6,5,5,8', queue)
    res = receive()
    print(res)

main()

