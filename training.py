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
    data_frames
    Data = pd.concat(data_frames, ignore_index=True)
    print("shape after reading =  ", Data.shape)
    return Data


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """clean_data [summary]

    Args:
        data (pd.DataFrame): [description]

    Returns:
        pd.DataFrame: [description]
    """
    #replace -99 entries with 0
    # data= data.replace(to_replace=-99 ,value= -99)
    print("shape after -99 replacements= ",data.shape)

    #Remove STEP rows
    data = data[data.iloc[:,5] != "STEP"]
    data= data.replace(np.nan,99)

    data =data.iloc[:,:-1].astype("int")
    mask5 = (data.iloc[:,2] == 5)  & (data.iloc[:,3] == 99  & data.iloc[:,3])
    data[mask5]  = data.replace(99,1)
    mask67 = (  (data.iloc[:,2] ==6) | (data.iloc[:,2] == 7) |(data.iloc[:,2] ==8)  ) & (data.iloc[:,3] == 99 & data.iloc[:,3])
    data[mask67] = data.replace(99,2)
    mask89 = (   (data.iloc[:,2] == 9) | (data.iloc[:,2] == 10) ) & (data.iloc[:,3] == 99 & data.iloc[:,3])
    data[mask89]  = data.replace(99,3)


    # mask4 = (  (data.iloc[:,2] ==10)   ) & (data.iloc[:,3] == 4 & data.iloc[:,3])
    # data[mask4]  = data.replace(4,5)



    print("mask")
    # print(mask.to_string())

    data= data.replace("STEP",np.nan)

    # data = data[data.iloc[:,1] <= 6 ]
    # data = data[data.iloc[:,1] >= 3 ]
    print("shape after Step replacements= ",data.shape)

    return data


def  Split_train_test(data: pd.DataFrame) :

    Y = data.iloc[:,3:4]
    X = data.iloc[:,4:]
    # Y = data.iloc[:,1:2]
    print("X y DONE")
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.05, random_state=0)
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

    print("Files after modification: ",files)

    Data = read_data(files)

    Data = clean_data(Data)
    print(Data.to_string())

    #split Data
    X_train, X_test, y_train, y_test = Split_train_test(Data)

    from sklearn import  ensemble
    from sklearn import tree    
    # model = svm.SVC(kernel='poly')
    # model = neighbors.KNeighborsClassifier()
    # model = linear_model.LinearRegression()
    model = ensemble.RandomForestClassifier(n_estimators=200, random_state=0)
    # model = tree.DecisionTreeClassifier( random_state=0)


    from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)

    model.fit(X_train , y_train )

    # import m2cgen as m2c
    # import sys
    # sys.setrecursionlimit(2147483647)
    # with open('./model.c','w') as f:
    #     code = m2c.export_to_c(model)
    #     f.write(code)



    import pickle
    filename = 'final.sav'
    pickle.dump(model, open(filename, 'wb'))
    # pickle.dump(sc, open("scaler.sav", 'wb'))

    # entry = X_test.iloc[15:16,:]
    # y_label3 = y_test.iloc[15,:]
    # print(entry)
    filename = 'final.sav'
    loaded_modelY = pickle.load(open(filename, 'rb'))

    y_pred = model.predict(X_test)
    print("prediction =     ",y_pred)
    print(list(y_test.values))
    


    print(model.score(X_test , y_test ))
    from sklearn import metrics

   
