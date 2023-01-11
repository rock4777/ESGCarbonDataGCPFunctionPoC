import config
import download as dl
import gcp_util as gcp


dl.getESGData(config.url, config.data_filter, config.headers)
df = dl.normESGData()
fileName = dl.exportESGtoCSV(df)
fileName = 'esg_clean_carbon_2023_01_11.csv'
gcp.upload_to_bucket(config.bucketName, fileName, fileName)
gcp.loadIntoBigQuery(fileName)