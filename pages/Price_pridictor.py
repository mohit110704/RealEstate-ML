import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.set_page_config(page_title="Viz Demo")
from joblib import load
# property_type	sector	bedRoom	bathroom	balcony	agePossession	built_up_area	servant room	store room	furnishing_type	luxury_category	floor_category

with  open('df.pkl','rb') as file:
    df=pickle.load(file)

pipeline = load('pipeline.pkl')

st.header("Enter Your Inputs")

# property_type

property_type=st.selectbox('Property Type',['flat','house'])

# Sector
sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

# bedroom
bedrooms=float(st.selectbox('Number of Bedrooms',sorted(df['bedRoom'].unique().tolist())))

# bathroom
bathroom=float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

# balcony
balcony=(st.selectbox(' Balconies',sorted(df['balcony'].unique().tolist())))

# property age

property_age=(st.selectbox('How much old property',sorted(df['agePossession'].unique().tolist())))


# built_Up_area
built_up_area=float(st.number_input('Built Up Area in sqft'))

# servent_room
servent_room=float(st.selectbox('Servent Room',[0.0,1.0]))

# store room
store_room=float(st.selectbox('Store Room',[0.0,1.0]))

# furnishing_type
furnishing_type=(st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist())))

# luxury_category
luxury_category=(st.selectbox('Luxury Type',sorted(df['luxury_category'].unique().tolist())))

# floor_category
floor_category=(st.selectbox('Floor Type',sorted(df['floor_category'].unique().tolist())))

if st.button('predict'):
    data=[[property_type,sector,bedrooms,bathroom,balcony,
           property_age,built_up_area,servent_room,store_room,
           furnishing_type,luxury_category,floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']
    # convert to dataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    # Predict
    base_price=np.expm1(pipeline.predict(one_df))[0]
    low=base_price-0.22
    high=base_price+0.22

    st.text('The price of the flat is between {} cr and {} cr'.format(round(low,2),round(high,2)))














