import pickle
import pandas as pd
import numpy as np
import pyrebase
import matplotlib.pyplot as plt
import time
import numpy as np
from sklearn.preprocessing import scale



configNew = {
    "apiKey": "AIzaSyBIFhbwdIXRf-TRlSvieuhw5VgnN4u9pp8",#Web API keyWeb API keyWeb API key
    "authDomain": "esp32data-e59a5.firebaseio.com", #Project ID.firebaseio.com
    "databaseURL": "https://esp32data-e59a5.firebaseio.com/",  #https://Project ID.firebaseio.com
    "projectId": "esp32data-e59a5", #Project ID
    "storageBucket": "esp32data-e59a5.firebaseio.com", #Project ID.firebaseio.com 
}

Firebase = pyrebase.initialize_app(configNew)


#load model
filename = 'final_model.sav'
loaded_modelY = pickle.load(open(filename, 'rb'))
Scaler = pickle.load(open("scaler.sav", 'rb'))
# loaded_modelX = pickle.load(open("finalized_model_svrX.sav", 'rb'))


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

   
    # print(result)
    return(resultX)





if __name__ == "__main__":

    filename = 'final.sav'
    loaded_modelY = pickle.load(open(filename, 'rb'))
    arr = np.array([[-47,0,-75,-99,-40,-56,-75,-55,-56]],dtype=int).T
    entry = pd.DataFrame(arr).transpose()
    print(entry.shape)
    result = loaded_modelY.predict(entry)
    
    print(result[0])

