import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import stool_db as sdb
import views as vw

db = sdb.Database('store.db')

#set page width
st.set_page_config(layout="wide")

#remove 'made with streamlit' footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#add sidebar data entry feed
st.sidebar.header("New Entry:")
cty = st.sidebar.radio("Consistency:",["Log","Pellet","Diarrhea"])
if cty == "Log":
    length = st.sidebar.slider("Length (inches):",0.25,24.0, step=.25)
    girth = st.sidebar.slider("Girth (inches):",0.05,4.0, step=.05)
    vol = st.sidebar.select_slider("Volume:",["Very Small","Small","Average","Large","Very Large"])
    bristol = st.sidebar.selectbox("Bristol classification:",[2,3,4])
if cty == "Pellet":
    length = 0
    girth = 0
    vol = st.sidebar.select_slider("Volume:",["Very Small","Small","Average","Large","Very Large"])
    bristol = st.sidebar.selectbox("Bristol classification:",[1,5,6])
if cty == "Diarrhea":
    length = 0
    girth = 0
    vol = st.sidebar.select_slider("Volume:",["Very Small","Small","Average","Large","Very Large"])
    bristol = 7
date = st.sidebar.date_input("Date passed:")
tagsList = st.sidebar.multiselect("Tags:",["Steamy","Spicy","Full-bodied","Pungent","Health concern","Weird color","Aroma",
    "Nutty","Caffeine","Nicotine","Boozy"])
if st.sidebar.button("Submit"):
    tags = ",".join(map(str,tagsList))
    db.insert(length,girth,vol,bristol,date,tags)
    vw.update_stools()
    st.success("Log successfully logged")

#separates our pages as functions
vw.mainView()
