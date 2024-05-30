import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors, Lipinski
import pandas as pd


# --------------------------------------------------------------
# Build lipinski descriptors
# --------------------------------------------------------------
def lipinski(smiles, verbose=False):

    moldata= []
    for elem in smiles:
        mol=Chem.MolFromSmiles(elem) 
        moldata.append(mol)
       
    baseData= np.arange(1,1)
    i=0  
    for mol in moldata:        
       
        desc_MolWt = Descriptors.MolWt(mol)
        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_NumHDonors = Lipinski.NumHDonors(mol)
        desc_NumHAcceptors = Lipinski.NumHAcceptors(mol)
           
        row = np.array([desc_MolWt,
                        desc_MolLogP,
                        desc_NumHDonors,
                        desc_NumHAcceptors])   
    
        if(i==0):
            baseData=row
        else:
            baseData=np.vstack([baseData, row])
        i=i+1      
    
    columnNames=["MW","LogP","NumHDonors","NumHAcceptors"]   
    descriptors = pd.DataFrame(data=baseData,columns=columnNames)
    
    return descriptors


# --------------------------------------------------------------
# Build morgan descriptors
# --------------------------------------------------------------
def morgan_descriptors(smiles: list):
    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
    
    fps = [AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048) for mol in mols]
    fps_array = [np.array(fp) for fp in fps]
    column_names = ['morgan_' + str(i) for i in range(len(fps_array[0]))]
    return pd.DataFrame(fps_array, columns=column_names)
