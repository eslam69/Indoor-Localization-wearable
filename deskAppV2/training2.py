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
d_lf = SVC(gamma=0.009,C=3150).fit(X,Y)
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