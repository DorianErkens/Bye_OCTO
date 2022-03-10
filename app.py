
from email import message
import pandas as pd
import streamlit as st

pd.set_option('max_colwidth',500)


DATA_URL =('https://erdo-streamlit-911.s3.eu-central-1.amazonaws.com/DB+-+ERDO+-+Octos+(4).csv')


st.title('ERDO out...')
data = pd.read_csv(DATA_URL)
#st.write(data.tail())
st.write("Merci pour tous les bons moments passés ensemble !")
st.write("Continuez à faire vivre OCTO comme jamais, continuez à être inspirants et ne lâchez rien :) ")
st.write("Un pot de départ est prévu le 17 mars pour ceux qui veulent fêter cela !")
polygramme=st.text_input("Remplis ton poly ici, j'ai laissé un mot doux")
data_bis=data[data.isin([polygramme]).any(axis=1)]
data_bis.reset_index(drop=True,inplace=True)
#data_bis=data_bis.drop(data_bis.iloc[:, 0])
#st.write(type(data_bis))
#data_bis=data_bis
#st.write('data_bis')
#st.write(data_bis)
if polygramme != "" :
    message=data_bis.Message.to_string()
    message = message[1:]
    st.write(message)
