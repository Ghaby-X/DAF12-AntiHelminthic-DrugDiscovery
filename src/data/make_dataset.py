# import logging
import pandas as pd
import os

# ---------------------------------------------------------------------------
# Script to process data from raw
# ---------------------------------------------------------------------------
def load_data_from_raw(path):
    df = pd.read_csv(path, nrows=30000)
    df = df[4:].set_index('PUBCHEM_RESULT_TAG') # remove first four rows and set index
    
    # define columns to keep
    if "S_STERCORALIS" in path:
        KEEP_COLUMNS = ['PUBCHEM_EXT_DATASOURCE_SMILES', 'PUBCHEM_ACTIVITY_OUTCOME', 'Activation at 6.8 uM']
    else:
        KEEP_COLUMNS = ['PUBCHEM_EXT_DATASOURCE_SMILES', 'PUBCHEM_ACTIVITY_OUTCOME', 'Average Activation at 6.8 uM']
        
    # map activities
    Activity = { 'Active': 1, 'Inactive': 0}
    df['PUBCHEM_ACTIVITY_OUTCOME'] = df['PUBCHEM_ACTIVITY_OUTCOME'].map(Activity)
    
    new_df = df[KEEP_COLUMNS]
    new_df.columns = ['SMILES', 'ACTIVITY', 'ACTIVATION_AT_6.8uM']
    
    
    return new_df


# ---------------------------------------------------------------------------
# Store dataframe as pickle 
# ---------------------------------------------------------------------------
def export(dataframe, path):
    
    if(not isinstance(dataframe, pd.DataFrame)) :
        raise TypeError('Object is not a pandas dataframe')
    
    dataframe.to_pickle(path)
    return

# ---------------------------------------------------------------------------
# main function
# ---------------------------------------------------------------------------
def main():
    # define paths to raw data and interim data
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_path = os.path.join(base_dir, '..', '..', 'data', 'raw')
    interim_data_path = os.path.join(base_dir, '..', '..', 'data', 'interim')
    
    
    # get data from raw_data path
    S_STERCORALIS_DATA = load_data_from_raw(os.path.join(raw_data_path, 'ASSAY_S_STERCORALIS.csv')) 
    H_GLYCINE_DATA = load_data_from_raw(os.path.join(raw_data_path, 'ASSAY_H_GLYCINE.csv')) 
    H_CONTORTUS_DATA = load_data_from_raw(os.path.join(raw_data_path, 'ASSAY_H_CONTORTUS.csv'))
    
    # save data to interim data path
    export(S_STERCORALIS_DATA, os.path.join(interim_data_path, '01_S_Stercoralis_processed.pkl'))
    export(H_GLYCINE_DATA, os.path.join(interim_data_path, '01_H_Glycine_processed.pkl'))
    export(H_CONTORTUS_DATA, os.path.join(interim_data_path, '01_H_Contortus_processed.pkl'))
    


if __name__ == '__main__':
    # logging config
    main()
