import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from micromlgen import port
from sklearn import neighbors



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
    print("shape after reading =  ", Data.shape)
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
    # data= data.replace(to_replace=-99 ,value= -999)
    print("shape after -99 replacements= ",data.shape)

    #Remove STEP rows
    data = data[data.iloc[:,3] != "STEP"]
    # data = data[data.iloc[:,1] <= 6 ]
    # data = data[data.iloc[:,1] >= 3 ]
    print("shape after Step replacements= ",data.shape)

    return data


def  Split_train_test(data: pd.DataFrame) :

    X = data.iloc[:,3:]
    # Y = data.iloc[:,1:2]
    Y = data.iloc[:,2:3]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=27)
    print("       ",Y.shape)
    print(X_train.shape,y_train.shape,y_test.shape)

    return X_train.astype('int'), X_test.astype('int'), y_train.astype('int'), y_test.astype('int')

    


if __name__ == "__main__":
    # create list of file names
    files = ["Data{}.xlsx".format(i) for i in range(1, 7)]
    # fix file 1 name
    print(files)
    files[0] = "Data1.xlsm"
    files[4] = "Data5.xlsm"
    # files.append("DataX3.xlsx")
    # files = files[-3:]

    print("Files after modification: ",files)

    Data = read_data(files)

    Data = clean_data(Data)
    # print(Data.to_string())

    #split Data
    X_train, X_test, y_train, y_test = Split_train_test(Data)


    
    # model = svm.SVC(kernel='poly')
    model = neighbors.KNeighborsClassifier()
    # model = linear_model.LinearRegression()

    model.fit(X_train , y_train )



    import pickle
    filename = 'finalized_model_SVC.sav'
    pickle.dump(model, open(filename, 'wb'))

    entry = X_test.iloc[15:16,:]
    y_label3 = y_test.iloc[15,:]
    print(entry)
    print("prediction =     ",model.predict(X_test))
    print(list(y_test.values))
    


    print(model.score(X_test , y_test ))

