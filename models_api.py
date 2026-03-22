import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd 

# Load models
random_forest = pickle.load(open("randomforest.sav", 'rb'))
decision_tree = pickle.load(open("decisiontree.sav", 'rb'))

# Sidebar menu

with st.sidebar:
    selected = option_menu(
        menu_title="Select The Model",
        options=["RandomForest model", "DecisionTree Model"],
        icons=["activity", "diagram-3"],  # optional
        default_index=0
    )

st.title('Heart Failure Survival Prediction')

if selected == "RandomForest model":
    st.header("Random Forest Model")
    serum_creatinine=st.text_input('What is patient Serum Creatinine?')
    ejection_fraction=st.text_input('What is patient Ejection Fraction?')
    age=st.text_input('What is the patient Age?')
    hf_survival=''
    if st.button('Heart Failure Survival'):
        hf_predict=random_forest.predict([[serum_creatinine,ejection_fraction,age]])
        if (hf_predict[0]==1):
            hf_survival='Will Not Survive'
        else:
            hf_survival='Will Survive'
    st.success(hf_survival)

elif selected == "DecisionTree Model":
    st.header("Decision Tree Model")

    serum_creatinine=st.text_input('What is patient Serum Creatinine?')
    ejection_fraction=st.text_input('What is patient Ejection Fraction?')
    age=st.text_input('What is the patient Age?')
    hf_survival=''
    if st.button('Heart Failure Survival'):
        hf_predict=random_forest.predict([[serum_creatinine,ejection_fraction,age]])
        if (hf_predict[0]==1):
            hf_survival='Will Not Survive'
        else:
            hf_survival='Will Survive'
    st.success(hf_survival)

    
