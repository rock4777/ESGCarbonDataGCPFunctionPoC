from google.cloud import functions_framework
import config
import download as dl
import gcp_util as gcp

@functions_framework.http
def esg_etl(request):
    dl.getESGData(config.url, config.dataFilter, config.headers)
    df = dl.normESGData()
    fileName = dl.exportESGtoCSV(df)
    fileName = 'esg_clean_carbon_2023_01_11.csv'
    gcp.upload_to_bucket(config.bucketName, fileName, fileName)
    gcp.loadIntoBigQuery(fileName)