# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
from pydoc import locate
from typing import List
import xgboost as xgb

import numpy as np
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import nest_asyncio

#nest_asyncio.apply()
model = pickle.load(open("model.dat", "rb"))
#model = xgb.Booster()
#model.load_model("model.json")


def create_type_instance(type_name: str):
    return locate(type_name).__call__()


def get_features_dict(model):
    d1=model.get_score()
    feature_types1 = [type(k) for k in d1.keys()]
    feature_names = model.get_score().keys()
    feature_types = list(map(create_type_instance, feature_types1))
    #return dict(zip(feature_names, feature_types))
    return dict(zip(model.get_score().keys(), model.get_score().values()))
    #return model.get_score()

def create_input_features_class(model):
    return type("InputFeatures", (BaseModel,), get_features_dict(model))


InputFeatures = create_input_features_class(model)
app = FastAPI()


@app.post("/predict", response_model=List)
async def predict_post(datas: List[InputFeatures]):
    return model.predict(np.asarray([list(data.__dict__.values()) for data in datas])).tolist()



if __name__ == "__main__":
    print(get_features_dict(model))
    uvicorn.run(app, host="0.0.0.0", port=8080)
