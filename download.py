import requests
import pandas as pd
from datetime import datetime
import config

#get ESG Data via API request and return DF
def getESGData (url, filter, headers):
    req = requests.post(url, json = filter, headers = headers, stream = True)
    with open("download.csv",'wb') as output_file:
        for chunk in req.iter_content(chunk_size=1025):
            if chunk:
                output_file.write(chunk)
    return print('Download Complete.')

def normESGData():
    df = pd.read_csv('download.csv',converters={'Sustainable Development Goals': convert_dtype})
    df.columns = df.columns.str.replace(' ', '')
    df.columns = df.columns.str.replace('/', '')
    df.index.rename('Key_Col', inplace=True)
    df.head()

    return df
    
def exportESGtoCSV(df):
    dt = "{:%Y_%m_%d}".format(datetime.now())
    filename = 'esg_clean_'+ config.esgDType + '_' + dt + '.csv'
    df.to_csv(filename)

    return filename

def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)   
    except:        
        return ''


