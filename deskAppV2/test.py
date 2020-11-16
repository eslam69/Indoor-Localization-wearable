import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.preprocessing import StandardScaler


def read_data(files: list) -> pd.DataFrame:
    """read_data [Reads a list of file names and concatenate them into one dataframe]

    Args:
        files (list): [a list of file names]

    Returns:
        pd.DataFrame: [All Data]
    """
    try:
        data_frames = [pd.read_excel(f) for f in files]
    except FileExistsError as e:
        print(e)
    Data = pd.concat(data_frames, ignore_index=True)
    # print(Data)
    # print(Data)
    return Data


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """clean_data [summary]

    Args:
        data (pd.DataFrame): [description]

    Returns:
        pd.DataFrame: [description]
    """
    #replace -99 entries with 0
    # data= data.replace(to_replace=-99 ,value= 0)
    # print("shape after -99 replacements= ",data.shape)

    #Remove STEP rows
    data = data[data.iloc[:,3] != "STEP"]
    print(data)

    
    return data

  


if __name__ == "__main__":
    # create list of file names
    files = ["Data{}.xlsx".format(i) for i in range(1, 4)]
    # fix file 1 name
    files[0] = "Data1.xlsm"
    print(files)

    Data = read_data(files)

    Data = clean_data(Data)

    sorted = np.linspace(0, 982, 982, endpoint=False)

    def cmp(a, b):
        return Data['STUDBME2'][int(a)] < Data['STUDBME2'][int(b)]
        
    sorted.sort(key=cmp)

    print(sorted)

    



    # print(model.score(X_test , y_test ))

