import requests # type: ignore
import os
import csv
import pandas as pd
import io
import pubchempy as pcp

SAVE_RAW_DATA_PATH = os.path.join('..','..','data', 'raw')

# assay data
ASSAY_H_GLYCINE = {'download_url': 'https://pubchem.ncbi.nlm.nih.gov/assay/pcget.cgi?query=download&record_type=datatable&actvty=all&response_type=save&aid=743050', 'title': 'H_Glycine_Assay_Data', 'save_path': os.path.join(SAVE_RAW_DATA_PATH, 'ASSAY_H_GLYCINE.csv')} #743050
ASSAY_H_CONTORTUS = {'download_url' : "https://pubchem.ncbi.nlm.nih.gov/assay/pcget.cgi?query=download&record_type=datatable&actvty=all&response_type=save&aid=743032", 'title': 'H_Contortus_Assay_Data', 'save_path': os.path.join(SAVE_RAW_DATA_PATH, 'ASSAY_H_CONTORTUS.csv')}
ASSAY_S_STERCORALIS = { 'download_url': "https://pubchem.ncbi.nlm.nih.gov/assay/pcget.cgi?query=download&record_type=datatable&actvty=all&response_type=save&aid=652126", 'title': 'Stercoralis_Assay_Data', 'save_path': os.path.join(SAVE_RAW_DATA_PATH, 'ASSAY_S_STERCORALIS.csv')}


'''
download data files from pubchem
'''

def download_file(assay_obj):
    
    print('download_file')
    # url = assay_obj.download_url
    # title = assay_obj.title
    # save_path = assay_obj.save_path
    
    # response = requests.get(url)
    
    # if response.status_code == 200:

    #     print(f"downloaded {title}")
    # else:
    #     print(f"Failed to download {title} file. Status code: {response.status_code}")

def main():

    print('main')

    
    # response = requests.get(ASSAY_S_STERCORALIS['download_url'])
    # content = response.content
    # df = pd.read_csv(io.BytesIO(content))
    # print(df.describe())
    # df.to_csv(ASSAY_S_STERCORALIS['save_path'])
    

        
    
if __name__ == '__main__':
    main()