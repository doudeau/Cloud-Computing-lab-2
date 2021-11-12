import boto3

# Get the service resource
sqs_client = boto3.client('sqs')
sqs_resources = boto3.resource('sqs')

queue_url_response = 'https://queue.amazonaws.com/976055184967/responseQueue'

def create_queue():
    # Create the queue. This returns an SQS.Queue instance
    return sqs_resources.create_queue(QueueName='requestQueue', Attributes={'DelaySeconds': '5'})
    

def send_numbers(numbers) :
    queue = create_queue()
    response = queue.send_message(
        MessageBody='boto3', 
        MessageAttributes={
            'Numbers': {
                'StringValue': numbers,
                'DataType': 'String'
                    }
    })

def response():
    try : 
        response = sqs_client.receive_message(
            QueueUrl=queue_url_response,
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

        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        res = message['MessageAttributes']['res']['StringValue']

        sqs_client.delete_message(
        QueueUrl=queue_url_response,
        ReceiptHandle=receipt_handle
        )
        print('Le résultat est : ', res)
        res = int(res)
        return res
    except:
        return None

def main():
    print('Entrez des nombres séparés par des virgules :')
    numbers = input()
    send_numbers(numbers)
    print('nombres envoyés')
    res = None
    while (res == None) :
        res = response()
    print('La moyenne est de : ')
    return 0
        
main()

