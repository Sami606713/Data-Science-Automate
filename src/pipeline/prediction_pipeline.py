import pandas as pd
import os
import numpy as np
import streamlit as st
import pickle as pkl
import logging
logging.basicConfig(level=logging.INFO)

def get_data(data):
    """
    This Fun is responsible for getting the data
    """
    result=predict(data=data)
    st.success(f"Predicted Price is: {np.round(result[0],3)}")
    
def predict(data):
    """
    This fun is responsible for predicting the price of the hosue
    """
    st.dataframe(data)
    try:
        logging.info("Load the model")
        model_path=os.path.join("models","best_model.pkl")
        process_path=os.path.join("models","processor.pkl")
        
        # Laod the process.pkl file
        with open(process_path,"rb") as f:
            process=pkl.load(f)
            logging.info("process loded successfully")
        process_data=process.transform(data)

        # Load the best model
        with open(model_path,"rb") as f:
            model=pkl.load(f)
            logging.info("Model loded successfully")
        logging.info("Prediction start")
        pred=model.predict(process_data)
        return pred
        
    except Exception as e:
        st.error("Model can't predict the price successfully")