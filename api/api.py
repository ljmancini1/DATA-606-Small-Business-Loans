# Dependencies
from flask import Flask, request, jsonify,json
import joblib
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if gbm:
        try:
            json_ = json.loads(request.data)
            query = pd.DataFrame.from_dict(json_)
            print(query)
            
            prediction = list(gbm.predict(query))
            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    gbm = joblib.load("./model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("./model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)
