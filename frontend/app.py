import numpy as np
from flask import Flask, jsonify, request, json
import tensorflow as tf
from numpy import array, concatenate
import pandas as pd
import json
import joblib
from sklearn.preprocessing import MinMaxScaler


#from pathlib import Path



#create my flask app Not much to say here. Set debug to False if you are deploying this API to production.
app = Flask(__name__)

#modeloDiario = Path('modeloDiario/')
#scaler = Path("testScaler")
#scalerLSTM = Path("scalerLSTM.save")
scaler = "testScaler"
scalerLSTM = "scalerLSTM.save"
#scaler = "/app/testScaler"
#scalerLSTM = "/app/scalerLSTM.save"

# Recreate the exact same model purely from the file
#importedMdl = tf.keras.models.load_model('/app/modeloDiario')
#importedLSTM = tf.keras.models.load_model('/app/LSTM')
importedMdl = tf.keras.models.load_model('modeloDiario/')
importedLSTM = tf.keras.models.load_model('LSTM/')


scaler_filename = scaler
scalar_filenameLSTM = scalerLSTM

importedScalar = joblib.load(scaler_filename)
importedScalarLSTM = joblib.load(scalar_filenameLSTM)


#print(importedScalar.data_max_)
#print(importedScalar.data_min_)

zero = array([[0]])
#X_test1 = arrOriginalay([[0.0,0.6,0.506944,0.6,0.055236,0.374126,0.724907,0.199052,0.786765,0.302954,0.261838,0.031014,0.35467,0.223484,0.405913,1.0,0.034749]])
#X_text1 = arrOriginalay([[1,4,4289948.83776,229.5,84.39582472,101.50930605,461.955377,942.071072,268.45742538,831.760486,5.17430607,1.62359422,16.2171337,49.20342242,90.52431235,29.19027778,944.87321779]])
#lstm
#X_test3 = array([[11375,40.333332,202,5.4166665,53,43.20833,232,3.8999991,5.2208343,6.8,1.1,1.8125,2.8,1.3,2.4833333,3,40.96,62.2125,75.75,8.3,12.595835,18.600002,951,955.25,959,0,1,1,2018,29.999998,6,12]]) 
#add a zero in a new column of arrOriginal

#lstm
#db_prediction1 = X_test3
#db_prediction1 = np.column_stack([X_test3,zero[:,-1]]) #works for month model

#lstm
#normalize
#np.set_printoptions(suppress=True)
#db_finalpred = importedScalarLSTM.transform(db_prediction1)
#lists2 = db_finalpred.tolist()
#print(db_finalpred)
#lstm
#db_finalpredReady = db_finalpred.reshape((db_finalpred.shape[0], 1, db_finalpred.shape[1]))

#print(db_finalpred.shape)
#print(lists2)
#lstm
#prediction2 = importedLSTM.predict(db_finalpredReady)

#print(prediction2)
#lstm

#db_finalpred[0][0] = prediction2
#inverted = importedScalarLSTM.inverse_transform(db_finalpred)

#print(inverted[0][0])




# routes
@app.route('/predictMontly', methods=['POST'])

def predict():
    
    # get data
    data = request.get_json(force=True)


    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)
    
    #convert dataframe to numpy array
    arrOriginal = data_df.to_numpy()
    
    #add a zero in a new column of arrOriginal
    db_prediction = np.column_stack([arrOriginal,zero[:,-1]])
    #normalize
    np.set_printoptions(suppress=True)
    db_finalpred = importedScalar.transform(db_prediction)
    
    arrOriginal = db_finalpred[:,:-1]

    
    jsonfiles = json.loads(data_df.to_json(orient='records'))
    
    lists = arrOriginal.tolist()
    json_str = json.dumps(lists)
        
    
    # predictions
    result = importedMdl.predict(arrOriginal)  
    
    #return jsonify(json_str2)
    
    predplusnormalized = np.column_stack([arrOriginal,result[:,-1]])
    inverted = importedScalar.inverse_transform(predplusnormalized)
    result = inverted[:,17]
    
    #predictionToInvert = concatenate((arrOriginal[:,:-1], result), axis=1)
    #predictionToInvert = importedScalar.inverse_transform(predictionToInvert)

    # send back to browser
    output = {'results': str(result)}

    
    # return data
    return jsonify(output)

@app.route('/predictDaily', methods=['POST'])
def predictLSTM():
    
    # get data
    data = request.get_json(force=True)


    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)
    
    #convert dataframe to numpy array
    arrOriginal = data_df.to_numpy()
    
    db_prediction1 = arrOriginal
    #normalize
    np.set_printoptions(suppress=True)
    db_finalpred = importedScalarLSTM.transform(db_prediction1)
    #lists2 = db_finalpred.tolist()
    #print(db_finalpred)
    
    #make it ready for the lstm
    db_finalpredReady = db_finalpred.reshape((db_finalpred.shape[0], 1, db_finalpred.shape[1]))
    
    
    jsonfiles = json.loads(data_df.to_json(orient='records'))
    lists = arrOriginal.tolist()
    json_str = json.dumps(lists)
        
    #make prediction
    prediction2 = importedLSTM.predict(db_finalpredReady)

    #print(prediction2)
    #inverse prediction
    db_finalpred[0][0] = prediction2
    inverted = importedScalarLSTM.inverse_transform(db_finalpred)
    
    result = inverted[0][0]
    #return jsonify(json_str2)

    #predictionToInvert = concatenate((arrOriginal[:,:-1], result), axis=1)
    #predictionToInvert = importedScalar.inverse_transform(predictionToInvert)

    # send back to browser
    output = {'results': str(result)}

    
    # return data
    return jsonify(output)

#when deploying to heroku we added host 00000
#host = '0.0.0.0', 

if __name__ == '__main__':
    app.run(port = 5000, debug=False)
	


