import os.path
from os import path
import requests
from urllib.request import urlopen
import csv
import streamlit as st
import altair as alt
import pandas as pd

st.title("ASSIGNMENT_4")
st.title("PART ONE")
st.title("Gender Equality Indicators 1960–2017.")
st.markdown(
"""
The World Bank tracks a number of different measures including fertility rate, literacy, employment and ownership of businesses, and wages to study the extent of gender equality around the world. The linked dataset curates a smaller subset of the overall set of gender indicators which you are welcome to use as well. 
""")

st.title("1/ Marks & Channels")
''' [See python code source] (https://github.com/TRABZI/dataAnalytics/blob/master/pySourceCode.py)
'''


st.header("Preparation of dataset")
''' We will visualize different aspects of gender equality around the world '''


#This is the url of the dataser gender.csv 
MY_URL_DATA = 'https://raw.githubusercontent.com/TRABZI/dataAnalytics/main/gender.csv'
'''
Firstly , we download the dataset from the following URL link :
[See URL link of dataset](https://raw.githubusercontent.com/TRABZI/dataAnalytics/main/gender.csv) '''


''' To do,  we define a function in python that downloads the csv file from the URL '''

#This is a definition of the function to download the csv from url defined above
with st.echo():
  def download_csv_data_from_url (CSV_URL_DATA):
    req=urlopen(CSV_URL_DATA)
    csv=req.read()
    csv_str=str(csv) # convert all to string
    lines=csv_str.split("\\n")
    file_url = 'CSV_downloaded'+".csv"
    fileopen=open(file_url,"w")
    for line in lines:
        fileopen.write(line+ "\n")
    fileopen.close()

#execute the function : download_csv_data_from_url
''' Now we execute the function download_csv_data_from_url(MY_URL_DATA)'''

''' The csv file is then Cleaned using openRefine to correct some errors, then we save flitered data in xls format '''

with st.echo():
	download_csv_data_from_url(MY_URL_DATA)

#print directory 
print(os.listdir())

csv_data=pd.read_csv("CSV_downloaded.csv",nrows=500)

df=pd.DataFrame(csv_data)
df.to_csv("gender_data_set.csv",index=False,sep='\t')

#The file gender_data_set.csv was filtered using openRefine , and then stored in xls format 
#Next we will be using the file Filtered_gender_data_set-csv.xls to make data visualizations 

#read xls file 
''' We will use a subset of the data to make visualizations'''
with st.echo():
	data=pd.read_excel("Filtered_gender_data_set-csv.xls", nrows=100,sep='\t')

#data size 
''' Data Size : use data.shape to see the data size '''
with st.echo():
	data.shape

'''we display the table of data (only some first rows) '''
with st.echo():
	chart =data.head()
	st.write(chart)

#display first rows of data
#data

st.header("Data Visualization Using Altair on Streamlit  (import streamlit as st & import altair as alt)")	

''' In the following we will visualize the informations in the dataset related to _ fertility rate, employment , and wages_ in order to study the extent of gender equality around the world . For each visualization we will make a brief analysis '''

st.header("Chart about Fertility rate")
with st.echo():
	chart=alt.Chart(data).mark_circle(filled=True).encode(
	    alt.X('Fertility rate, total (births per woman):Q'),
	    alt.Y('CountryName:N'),
	    alt.Tooltip('CountryName'),
	).properties(width=935, height=735)
	st.write(chart)
''' Analysis of the above chart : We made this chart in order to highlight the fertility in several countries in the world. To this end, we represent in the X axis the Fertility rate and in Y axis the countries. This representation is very easy to read and it is not misleading , we juste need to read the name of country and then see the values of the attributes. We chosed to make Country Names in Y axis to make it easier to read the countries names. The mark choosed is circle. We could also use bars to make the same visualization by using mark_bar.  '''

st.header("Chart about Female Employment")
with st.echo():
		chart=alt.Chart(data).mark_circle(filled=True).encode(
		    alt.X('Employment to population ratio, 15+, female (%) (modeled ILO estimate):Q'),
		    alt.Y('CountryName:N'),
		    alt.OpacityValue(0.5),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=735)
		st.write(chart)

''' Analysis of the above chart: This chart give an idea about female employement in some countries around the world.The X axis (Employment to population ratio, 15+, female) and Y axis the counries name. This chart still easy to understand because it is based on simple representation with circles '''


st.header("Chart about male Employment")
with st.echo():
		chart=alt.Chart(data).mark_bar(filled=True).encode(
		    alt.Y('Employment to population ratio, 15+, male (%) (modeled ILO estimate):Q'),
		    alt.X('CountryName:N'),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=535)
		st.write(chart)

''' Chart above is representing the male Employment to population ratio in some countries in the world . The mark used is bars. This chart is easy to understand and to read '''


st.header("Chart about wage & salaried workers (male and female)")
with st.echo():
		chart=alt.Chart(data).mark_bar().encode(
		    alt.X('CountryName:N'),
		    alt.Y('Wage and salaried workers, male (% of male employment) (modeled ILO estimate):Q'),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=535)
		
		st.write(chart)

''' Chart above is representing the male pourcentage of salaried workers in some countries in the world . The mark used is bars. This chart is easy to understand and to read  '''


st.title("2/ Data Transformations")

st.markdown(
""" Here we will explore methods for transforming data, including the use of aggregates to summarize multiple records. Data transformation is an integral part of visualization: choosing the variables to show and their level of detail is just as important as choosing appropriate visual encodings. After all, it doesn't matter how well chosen your visual encodings are if you are showing the wrong information! """)


st.header("summarize data ")
with st.echo():
	chart=alt.Chart(data).mark_circle(filled=True).encode(
	    alt.X('Fertility rate, total (births per woman):Q', bin=True),
	    alt.Y('CountryName:N'),
	    alt.Tooltip('CountryName'),
	).properties(width=635, height=735)
	st.write(chart)
'''To summarize this data, we can bin a data field to group numeric values into discrete groups. Here we bin along the x-axis by adding bin=True to the x encoding channel. The result is a set of bins (16) of equal step size, each corresponding to a span of 0,5 ratings points.
'''

st.header("Filter Data")

'''
The filter transform creates a new table with a subset of the original data. Bellow we apply a filter to limite our plot and for example showing the data only for a specific country for instance we choose "Haiti"
'''
with st.echo():
	chart=alt.Chart(data).mark_circle(filled=True).encode(
	    alt.X('Fertility rate, total (births per woman):Q'),
	    alt.Y('Year:N'),
	    alt.Color('CountryName:N'),
	    alt.Tooltip('CountryName'),
	).properties(width=535, height=335).transform_filter('datum.CountryName == "Haiti" ')
	st.write(chart)
''' This chart is obtained by filtering the dataset by keeping only one specific country to be presented in the chart in order to highlight its specific informations, this make it more easier if we are interested only in a specific country to be studied. '''
