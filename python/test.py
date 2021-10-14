import boto3

# Get the service resource
sqs = boto3.resource('sqs')

def create_queue():
    # Create the queue. This returns an SQS.Queue instance
    return sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})
    

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
    print(queue.url)


def main():
    queue = create_queue()
    send_numbers('2,5,6,3,8,9,4,6,5,5,8', queue)

main()

