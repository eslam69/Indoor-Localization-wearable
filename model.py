import pickle
import pandas as pd
import numpy as np
import pyrebase
import matplotlib.pyplot as plt
import time
import numpy as np


configNew = {
    "apiKey": "AIzaSyBIFhbwdIXRf-TRlSvieuhw5VgnN4u9pp8",
    "authDomain": "esp32data-e59a5.firebaseio.com",
    "databaseURL": "https://esp32data-e59a5.firebaseio.com/",
    "projectId": "esp32data-e59a5",
    "storageBucket": "esp32data-e59a5.firebaseio.com",
}

Firebase = pyrebase.initialize_app(configNew)


#load model
filename = 'finalized_model_svr.sav'
loaded_modelY = pickle.load(open(filename, 'rb'))
loaded_modelX = pickle.load(open("finalized_model_svrX.sav", 'rb'))


def get_data(firebase=None):
    if firebase == None:
        firebase = Firebase

    db = firebase.database()
    data = db.child("readings").get()
    return(data.val())

def parse_data(data: str)->list :
    rss_list= data.split(",")
    if len(rss_list) == 9:
        rss_list = [int(wifi) for wifi in rss_list ]
        return(rss_list)
    else :
        print("Invalid Data from Fire base")
        quit()


def get_coordinates(rss_list:list):
    #get string of 9 rss with delimeter ","
    #parse the string into a list
    # rss_list = parse_data(raw_entry)
    
    arr = np.array(rss_list,dtype=int).T
    entry = pd.DataFrame(arr).transpose()
    resultX = loaded_modelY.predict(entry)[0]
    resultY = loaded_modelX.predict(entry)[0]
    result = [resultX, resultY]
    # print(result)
    return(result)





if __name__ == "__main__":

    filename = 'finalized_model_svr.sav'
    loaded_modelY = pickle.load(open(filename, 'rb'))
    arr = np.array([-99, -58,  -99, -99,  -65,   -99,  -99,  -99,   -99],dtype=int).T
    entry = pd.DataFrame(arr ).transpose()
    print(entry.shape)
    result = loaded_modelY.predict(entry)
    
    print(result[0])

