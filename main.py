# from google.cloud import functions_framework
import config
import download as dl
import gcp_util as gcp

# @functions_framework.http
# def esg_etl(request):
dl.getESGData(config.url, config.dataFilter, config.headers)
df = dl.normESGData()
fileName = dl.exportESGtoCSV(df)
gcp.uploadToBucket(config.bucketName, fileName, fileName)
gcp.loadIntoBigQuery(fileName)