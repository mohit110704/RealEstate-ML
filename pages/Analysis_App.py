import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")


st.title("Analytics")

new_df=pd.read_csv('Datasets/data_viz1.csv')
feature_text=pickle.load(open('Datasets/feature_text.pkl','rb'))

group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean().reset_index()

st.header('Sector Price per sqft GeoMap')
fig=px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=600
                      ,hover_name=group_df.index)
st.plotly_chart(fig,use_container_width=True)


# WordCloud
st.header('Features WordCloud')
wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig)

# Area vs Price Scatter Plot
st.header('Area vs Price')
property_type=st.selectbox('select property type',['flat','house'])
if property_type=='house':
    fig1 = px.scatter(new_df[new_df['property_type']=='house'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type']=='flat'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, use_container_width=True)

# Pie Chart

st.header('BHK Pie Chart')
sector_options=new_df['sector'].unique().tolist()
sector_options.insert(0,'Overall')
selected_sector=st.selectbox('select Sector',sector_options)
if selected_sector=='Overall':
    fig2 = px.pie(new_df, names="bedRoom")
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector']==selected_sector], names="bedRoom")
    st.plotly_chart(fig2, use_container_width=True)

# Boxplot of Bedrooms
st.header('Side by side BHK Price comparison')
fig3=px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True)

# distribution plot
st.header('Price distribution Flat vs House ')
fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(new_df[new_df['property_type'] == 'house']['price'],
             kde=True, color="blue", label="House", ax=ax)
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'],
             kde=True, color="green", label="Flat", ax=ax)

ax.set_xlabel("Price")
ax.set_ylabel("Frequency")
ax.legend()

st.pyplot(fig)