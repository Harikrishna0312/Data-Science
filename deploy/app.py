import streamlit as st
from pickle import load
import pandas as pd


st.title('Classification Model')
st.write('Will they hire an attorney?')


def load_page():
	age = st.sidebar.slider('Age', min_value=18, max_value=100)
	insur = st.sidebar.checkbox ('Life Insurance Available' )
	sex = st.sidebar.radio('Gender', ['Male','Female'])
	seat = st.sidebar.checkbox ('Seatbelt' )
	amt = st.sidebar.number_input ('Enter Claim Amt')


	if sex == 'Male':
		sex = 1
	else:
		sex = 0


	data = {
	'CLMSEX'	: sex,
	'CLMINSUR'	: insur,
	'SEATBELT'	: seat,
	'CLMAGE'	: age,  	
	'LOSS'		: amt
	}

	df = pd.DataFrame(data, index=[0])

	return df



loaded_model = load(open('clf.pkl', 'rb'))

features = load_page()

if st.sidebar.button('Submit'):
	st.write(features)
	predicted = loaded_model.predict(features)
	if predicted == 0 :
		st.write('No, they will not hire an attorney')
	else:
		st.write('Yes, they will hire an attorney')


