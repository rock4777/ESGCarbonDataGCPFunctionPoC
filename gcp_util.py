from google.cloud import storage
from google.cloud import bigquery

def uploadToBucket(bucket_name, blob_path, local_path):
    bucket = storage.Client().bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_path)

    return print('Upload Success!')

def loadIntoBigQuery(fileName):
    client = bigquery.Client()
    query = '''LOAD DATA OVERWRITE esg_poc.esgCarbon
        FROM FILES (
        format = 'CSV',
        uris = ['gs://esg_poc/''' + fileName +'''']);'''
    client.query(query)  # API request
    
    return print('Big Query Load Success')