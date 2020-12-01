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
from sklearn.svm import SVC
from micromlgen import port
import pandas as pd
from sklearn.metrics import precision_score
import math

def read_data(files: list) -> pd.DataFrame:
    try:
        data_frames = [pd.read_excel(f) for f in files]
    except FileExistsError as e:
        print(e)
    Data = pd.concat(data_frames, ignore_index=True)
    return Data


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data[data.iloc[:, :] != "STEP"]
    # data = data.dropna()
    # data = data[math.isnan(float(data.iloc[:, :]))  ]
    # x = float('nan')
    

    return data


def splitTrainTest(data: pd.DataFrame):
    X = data.iloc[:1173, 4:13]
    Y = data.iloc[:1173, 2:3]
    xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size=0.1, random_state=5)

    return xTrain.astype('int'), xTest.astype('int'), yTrain.astype('int'), yTest.astype('int')


if __name__ == "__main__":
    files = ["Data{}.xlsx".format(i) for i in range(1, 7)]
    files[0] = "Data1.xlsm"
    files[4] = "Data5.xlsm"

    Data = read_data(files)
    print("done reading")
    # print(Data.to_string())

    Data = clean_data(Data)
    print("done cleaning")
    print(Data.to_string())

    # split Data
    # xTrain, xTest, yTrain, yTest = splitTrainTest(Data)
    # print(type(xTrain))

    # print(xTrain.to_string())

    # model = svm.SVR(kernel='poly')
    # model.fit(X_train , y_train )

    # model = SVC(gamma=0.009, C=3150).fit(xTrain, yTrain)
    # print("prediction=", model.predict(xTest))
    # print("TRUE_VALUE=", yTest)


    import pickle

    # filename = 'trainedModel.sav'
    # pickle.dump(model, open(filename, 'wb'))

    # entry = X_test.iloc[15:16, :]
    # y_label3 = y_test.iloc[15, 0]
    # print(entry)
    # print("prediction =     ",model.predict(X_test))
    # print(list(y_test.values))

    # print(model.score(X_test , y_test ))

"""
from sklearn.svm import SVC
from micromlgen import port
import pandas as pd
from firebase import firebase
from sklearn.metrics import precision_score



#firebase = firebase.FirebaseApplication('https://localization-aeca4.firebaseio.com/', None)
#result = firebase.get('/f_data', None)
#print(result)

#import sklearn.model_selection import train_test_split
X = pd.read_csv("v2.csv")[['STUDBME2', 'memo', 'HTC Portable Hotspot 1425', 'HUAWEI Y9 2019']]
Y = pd.read_csv("v2.csv")['y']
#print(X.shape )
#print(Y.shape)
d_lf =SVC(gamma=0.009,C=3150).fit(X,Y)
print("prediction=", d_lf.predict(X))
print("prediction2=", d_lf.predict([[-54	,	-99,	-44,	-60]]))
print("TRUE_VALUE=",Y[100])

precision = precision_score(Y,d_lf.predict(X) , average='macro')
print("PRECISION=",precision)


testscore= d_lf.score(X,Y)
print("acc=" , testscore )
c_code = port(d_lf)

with open('code.h','w') as f:
    f.write(c_code)
#print("result =",result)
#print("acc =",testAcc*100 ,"%")

#print(Y)
#rf = RandomForestClassifier(n_estimators=6, max_depth=20) # n_estimators=6
# rf.fit(X_train, y_train)
#rf.fit(X, Y)

# first_row = X_test[0]
# print(first_row)
#print("prediction:", rf.predict([[-72, -55, -83, -75, -73]]))  **give point to the model to prediction
#print("true value:", Y[212])                                   ** the true prediction
#print("random forest accuracy:", rf.score(X, Y))
#print('data dimensions', X.shape)
"""
