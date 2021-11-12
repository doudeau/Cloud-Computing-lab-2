import boto3
import random
import json

# Nom du bucket
BUCKET2 = "lab2-result"

s3 = boto3.resource('s3')

# Permet d'enregistrer une photo dans le bucket
def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

# Retourne une liste des urls de toutes les photos du bucket afin de les afficher
def show_image(bucket):
    s3_client = boto3.client('s3')
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    return public_urls

# def choose4bis(tab) :
#     res = []
#     alreadyTake=[]
#     while len(alreadyTake)<4 :
#         indice = random.randrange(0,len(tab))
#         if indice not in alreadyTake:
#             alreadyTake.append(indice)
#             res.append(tab[indice])
#     return [res,alreadyTake]

# Retourne 4 photos aléatoires du bucket avec leur indices carrespondants
def choose4(tab):
    indices = random.sample(range(len(tab)), 4)
    res = []
    for k in indices :
        res.append(tab[k])
    return [res, indices]

# Retourne la liste de tous les objets (photos) du bucket
def getListPics(bucket):
    s3_client = boto3.client('s3')
    list = s3_client.list_objects(Bucket = bucket)
    return list

# Retourne le nom des photos correspondant aux indices donnés
def getIdList(listPics,indices):
    res = []
    for i in indices:
        res.append(listPics['Contents'][i]['Key'])
    return res

# recupère sur le bucket le fichier de resultat (json) et le retourne
def downloadResult():
    s3 = boto3.client('s3')
    content_object = s3.get_object(Bucket=BUCKET2, Key='result.json')
    file_content = content_object['Body']
    return json.load(file_content)