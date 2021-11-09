import boto3
import random

# Let's use Amazon S3
s3 = boto3.resource('s3')

# s3 = boto3.resource(
#     service_name='s3',
#     region_name='us-east-1',
#     aws_access_key_id='ASIASHD7MVLFQ5CO5SVR',
#     aws_secret_access_key='KubxkPhKWBFAsPXYycbQ97Ku4Pc8JDc5YSSk8eet'
# )
# for bucket in s3.buckets.all():
#     print(bucket.name)

# for obj in s3.Bucket('lab2-doggy-doggo').objects.all():
#     print(obj)

def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def show_image(bucket):
    s3_client = boto3.client('s3')
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    # print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls

def choose4(tab) :
    res = []
    alreadyTake=[]
    while len(alreadyTake)<4 :
        indice = random.randrange(0,len(tab))
        if indice not in alreadyTake:
            alreadyTake.append(indice)
            res.append(tab[indice])
    return [res,alreadyTake]