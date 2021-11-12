import boto3
import time

# Create SQS client
sqs_client = boto3.client('sqs')
sqs_resources = boto3.resource('sqs')

queue_url_request = 'https://queue.amazonaws.com/976055184967/requestQueue'

def response():
    try :
        response = sqs_client.receive_message(
            QueueUrl=queue_url_request,
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
        numbers = message['MessageAttributes']['Numbers']['StringValue']

        sqs_client.delete_message(
        QueueUrl=queue_url_request,
        ReceiptHandle=receipt_handle
        )
        print('les chiffres sont : ', numbers)
        numbersList = list(map(int,numbers.split(',')))
        return numbersList
    except :
        return None

def compute(numbers) :
    res = 0
    for i in numbers :
        res +=i
    return res/len(numbers)

def create_queue():
    # Create the queue. This returns an SQS.Queue instance
    return sqs_resources.create_queue(QueueName='responseQueue', Attributes={'DelaySeconds': '5'})

def sendAnswer(answer) :
    queue = create_queue()
    response = queue.send_message(
        MessageBody='boto3', 
        MessageAttributes={
            'res': {
                'StringValue': answer,
                'DataType': 'String'
                    }
    })


def main():
    numbers = None
    while (numbers == None) :
        numbers = response()
    print('nombres recus')
    res= compute(numbers)
    print('reponse envoyée')
    sendAnswer(str(res))
    return 0
    

main()



