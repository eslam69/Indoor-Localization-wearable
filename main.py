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
    print("shape after reading=  ",Data.shape)
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
    data= data.replace(to_replace=-99 ,value= 0)
    print("shape after -99 replacements= ",data.shape)

    #Remove STEP rows
    data = data[data.iloc[:,3] != "STEP"]
    print("shape after Step replacements= ",data.shape)

    
    return data


def  Split_train_test(data: pd.DataFrame) :

    X = data.iloc[:,2:]
    Y = data.iloc[:,1:2]
    # sc_x  = StandardScaler()
    # sc_y = StandardScaler()
    # X = sc_x.fit_transform(X)
    # Y = sc_x.fit_transform(Y)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=4)
    print("       ",Y.shape)
    print(X_train.shape,y_train.shape,y_test.shape)

    return X_train.astype('int'), X_test.astype('int'), y_train.astype('int'), y_test.astype('int')

    


if __name__ == "__main__":
    # create list of file names
    files = ["Data{}.xlsx".format(i) for i in range(1, 4)]
    # fix file 1 name
    files[0] = "Data1.xlsm"
    print(files)

    Data = read_data(files)

    Data = clean_data(Data)
    # print(Data.to_string())

    #split Data
    X_train, X_test, y_train, y_test = Split_train_test(Data)

    # classifier = svm.SVC(kernel='poly',random_state=4,degree=9)
    # classifier.fit(X_train , y_train )

    
    model = svm.SVR(kernel='poly')
    model.fit(X_train , y_train )



    print(model.score(X_test , y_test ))

