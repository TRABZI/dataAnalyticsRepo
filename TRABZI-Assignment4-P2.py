import os.path
from os import path
import requests
from urllib.request import urlopen
import streamlit as st
import altair as alt
import pandas as pd  
import sys
import csv	
print('you can run this code on streamlit by writing the commande : streamlit run TRABZI-Assignment4-P2.py') 

st.title("ASSIGNMENT_4")
st.title("PART ONE")
st.title("Gender Equality Indicators 1960–2017.")

st.markdown(
"""
The World Bank tracks a number of different measures including fertility rate, literacy, employment and ownership of businesses, and wages to study the extent of gender equality around the world. The linked dataset curates a smaller subset of the overall set of gender indicators which you are welcome to use as well. [See python code source] (https://github.com/TRABZI/dataAnalyticsRepo/tree/master)
""")

st.title("1/ Marks & Channels")
''' [See python code source] (https://github.com/TRABZI/dataAnalyticsRepo/tree/master) '''

st.header("Preparation of dataset")
''' We will visualize different aspects of gender equality around the world '''


#This is the url of the dataser gender.csv 
MY_URL = 'https://raw.githubusercontent.com/TRABZI/dataAnalyticsRepo/main/gender.csv'

''' Firstly , we download the dataset from the following URL link :
[See URL link of dataset](https://github.com/ZeningQu/World-Bank-Data-by-Indicators/blob/master/gender/gender.csv) 
'''


''' To do,  we define a function in python that downloads the csv file from the URL '''
print('to execute this code you have download xls file from this link : https://github.com/TRABZI/dataAnalyticsRepo/blob/master/Filtered_gender_data_set-csv.xls')
#This is a definition of the function to download the csv from url defined above
with st.echo():
  def download_csv_data_from_url(CSV_URL_DATA):
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
with st.echo():
	download_csv_data_from_url(MY_URL)
''' IMPORTANT REMARQUE : '''
''' The downloaded csv file is then filtered using openRefine to correct some errors, then we save flitered data in xls format [Download the xls file](https://github.com/TRABZI/dataAnalyticsRepo/blob/master/Filtered_gender_data_set-csv.xls) '''
'''Download the xls file then re run the code with command : streamlit run code_p2.py'''
''' Make sur you have downloaded the xls file from this link [Download the xls file](https://github.com/TRABZI/dataAnalyticsRepo/blob/master/Filtered_gender_data_set-csv.xls)'''

#print directory 
print('\n -> you repository')
print(os.listdir())

csv_data=pd.read_csv("CSV_downloaded.csv",nrows=500)

df=pd.DataFrame(csv_data)
df.to_csv("gender_data_set.csv",index=False,sep='\t')

print('The file gender_data_set.csv was filtered using openRefine , and then stored in xls format')
print('Next we will be using the file Filtered_gender_data_set-csv.xls to make data visualizations') 

#read xls file 
''' We will use a subset of the data to make visualizations'''
''' Make sur you have downloaded the xls file from this link [Download the xls file](https://github.com/TRABZI/dataAnalyticsRepo/blob/master/Filtered_gender_data_set-csv.xls)'''

try:
    f=open('Filtered_gender_data_set-csv.xls')
    f.close()
except FileNotFoundError:
	print('the file Filtered_gender_data_set-csv.xls is not existing in your repository, please download it from this link : https://github.com/TRABZI/dataAnalyticsRepo/blob/master/Filtered_gender_data_set-csv.xls')
	sys.exit(2)

	
data=pd.read_excel("Filtered_gender_data_set-csv.xls", nrows=100,sep='\t')
with st.echo():
	data=pd.read_excel("Filtered_gender_data_set-csv.xls", nrows=100,sep='\t')

#data size 
''' Data Size : use data.shape to see the data size '''
with st.echo():
	data.shape

#display first rows of data
data.head(5)

'''we display the table of data '''
with st.echo():
	data


st.header("Data Visualization Using Altair on Streamlit  (import streamlit as st & import altair as alt)")	

''' In the following we will visualize the informations in the dataset related to fertility rate, literacy, employment and ownership of businesses, and wages to study the extent of gender equality around the world . For each visualization we will make a brief analysis '''

st.header("Chart about Fertility rate")
with st.echo():
	chart=alt.Chart(data).mark_point(filled=True).encode(
	    alt.Color('Year:Q',scale=alt.Scale(zero=False)),
	    alt.X('Fertility rate, total (births per woman):Q'),
	    alt.Size('Adolescent fertility rate (births per 1,000 women ages 15-19):Q',scale=alt.Scale(range=[0,2000])),
	    alt.Y('CountryName:N'),
	    alt.OpacityValue(0.5),
	    alt.Shape('Country Code:N'),
	    alt.Tooltip('CountryName'),
	).properties(width=935, height=735)
	st.write(chart)
	
''' Analysis of chart above: We made this chart in order to highlight the fertility in several countries in the world by using more attributes to get more complex visualization. To this end, we represent in the X axis the Fertility rate and in Y axis the Country Name. Also, with sizing circles we encode the Adolescent fertility rate (births per 1,000 women ages 15-19), we made this choice because it has a direct relation with the attribute we represented in X axis. And finally we use color hue to encode years. The more the circle is big and pointed in the right part of the chart the more is the Fertility in the country and vise versa '''
''' The filtering is then applied on this chart by sorting of Y axis depending on other attribute in order to change the shape of the chart .'''
with st.echo():
	chart=alt.Chart(data).mark_point(filled=True).encode(
	    alt.Color('Year:Q',scale=alt.Scale(zero=False)),
	    alt.X('Fertility rate, total (births per woman):Q'),
	    alt.Size('Adolescent fertility rate (births per 1,000 women ages 15-19):Q',scale=alt.Scale(range=[0,2000])),
	    alt.Y('CountryName:N',sort=alt.EncodingSortField(
		    field='Adolescent fertility rate (births per 1,000 women ages 15-19)', order='descending')
		    ),
	    alt.OpacityValue(0.5),
	    alt.Shape('Country Code:N'),
	    alt.Tooltip('CountryName'),
	).properties(width=935, height=835)
	st.write(chart)
	
	
st.header("Chart about Female Employment")
with st.echo():
		chart=alt.Chart(data).mark_point(filled=True).encode(
		    alt.Color('Employment to population ratio, ages 15-24, female (%) (modeled ILO estimate):Q'),
		    alt.X('Employment to population ratio, 15+, female (%) (modeled ILO estimate):Q'),
		    alt.Size('Part time employment, female (% of total female employment):Q',scale=alt.Scale(range=[0,2000])),
		    alt.Y('CountryName:N'),
		    alt.OpacityValue(0.5),
		    alt.Shape('Country Code:N'),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=835)
		st.write(chart)
''' Analysis of chart above: This chart give and idea about female employement in some countries around the world.The X axis (Employment to population ratio, 15+, female) and Y axis for Country Name and color hue for Employment to population ratio, ages 15-24, and the rate of part time employement of female is encoded with size of circles. The attributes are multiple in this chart and represents lot of details . This chart highlights the Employement of female and also the rate of Part time employement   '''
''' We change the shape of this chart by using sort '''

with st.echo():
		chart=alt.Chart(data).mark_point(filled=True).encode(
		    alt.Color('Employment to population ratio, ages 15-24, female (%) (modeled ILO estimate):Q'),
		    alt.X('Employment to population ratio, 15+, female (%) (modeled ILO estimate):Q'),
		    alt.Size('Part time employment, female (% of total female employment):Q',scale=alt.Scale(range=[0,2000])),
		    alt.Y('CountryName:N',sort=alt.EncodingSortField(
		    field='Part time employment, female (% of total female employment)', order='descending')
		    ),
		    alt.OpacityValue(0.5),
		    alt.Shape('Country Code:N'),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=735)
		st.write(chart)

st.header("Chart about male Employment")
with st.echo():
		chart=alt.Chart(data).mark_point(filled=True).encode(
		    alt.X('Employment to population ratio, 15+, male (%) (modeled ILO estimate):Q'),
		    alt.Color('Employment to population ratio, ages 15-24, male (%) (modeled ILO estimate):Q'),
		    alt.Size('Part time employment, male (% of total male employment):Q',scale=alt.Scale(range=[0,2000])),
		    alt.Y('CountryName:N'),
		    alt.OpacityValue(0.5),
		    alt.Shape('Country Code:N'),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=635)
		st.write(chart)

''' Chart above is the same as the previous one , only we change Female by Male '''

with st.echo():
		chart=alt.Chart(data).mark_point(filled=True).encode(
		    alt.X('Employment to population ratio, 15+, male (%) (modeled ILO estimate):Q'),
		    alt.Color('Employment to population ratio, ages 15-24, male (%) (modeled ILO estimate):Q'),
		    alt.Size('Part time employment, male (% of total male employment):Q',scale=alt.Scale(range=[0,2000])),
		    alt.Y('CountryName:N',sort=alt.EncodingSortField(
		    field='Part time employment, male (% of total male employment)', order='descending')
		    ),
		    alt.OpacityValue(0.5),
		    alt.Shape('Country Code:N'),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=635)
		st.write(chart)
		
st.header("Chart about wage & salaried workers (male and female)")
with st.echo():
		chart=alt.Chart(data).mark_bar().encode(
		    alt.X('Wage and salaried workers, male (% of male employment) (modeled ILO estimate):Q'),
		    alt.Y('CountryName:N'),
		    alt.Size('Wage and salaried workers, female (% of female employment) (modeled ILO estimate):Q'),
		    alt.OpacityValue(0.5),
		    alt.Color('Country Code:N'),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=735)
		st.write(chart)

''' The  Chart above is representing in the same time the rate of male & female salaried workers in some countries in the world, so that we can notice the differences . The X axis the rate of salaried male workers , Y axis represents country Names , The salaried female rate is represented with size , and we use color to represent Country Code  . '''
''' Then we use sort to change the shape if the chart '''
with st.echo():
		chart=alt.Chart(data).mark_bar().encode(
		    alt.X('Wage and salaried workers, male (% of male employment) (modeled ILO estimate):Q'),
		    alt.Y('CountryName:N',sort=alt.EncodingSortField(
		    field='Wage and salaried workers, male (% of male employment) (modeled ILO estimate)', order='descending')
		    ),
		    alt.Size('Wage and salaried workers, female (% of female employment) (modeled ILO estimate):Q'),
		    alt.OpacityValue(0.5),
		    alt.Color('Country Code:N'),
		    alt.Tooltip('CountryName'),
		).properties(width=935, height=735)
		st.write(chart)

st.title("2/ Data Transformations")

st.markdown(
""" Here we will explore methods for transforming data, including the use of aggregates to summarize multiple records. Data transformation is an integral part of visualization: choosing the variables to show and their level of detail is just as important as choosing appropriate visual encodings. After all, it doesn't matter how well chosen your visual encodings are if you are showing the wrong information! """)


st.header("summarize data ")
with st.echo():
	chart=alt.Chart(data).mark_circle(filled=True).encode(
	    alt.Y('Year:Q',scale=alt.Scale(zero=False),bin=alt.BinParams(maxbins=20)),
	    alt.X('Fertility rate, total (births per woman):Q', bin=alt.BinParams(maxbins=20) ),
	    alt.Size('Adolescent fertility rate (births per 1,000 women ages 15-19):Q',scale=alt.Scale(range=[0,3000])),
	    alt.Color('CountryName:N'),
	    alt.OpacityValue(0.4),
	    alt.Tooltip('CountryName'),   
	).properties(width=635, height=735)
	st.write(chart)
'''To summarize this data, we can bin a data field to group numeric values into discrete groups. Here we bin along the x-axis & y-axis by adding BinParams(maxbins=20) to the x & y encoding channel. The result is a set of bins of equal step size.
'''

st.header("Filter Data")

'''
The filter transform creates a new table with a subset of the original data. Bellow we apply a filter to limite our plot and for example showing the data only for specific years for instance we choose "year>2010"
'''
with st.echo():
	chart=alt.Chart(data).mark_circle(filled=True).encode(
	    alt.Y('Year',scale=alt.Scale(zero=False)),
	    alt.X('Fertility rate, total (births per woman):Q',scale=alt.Scale(zero=False)),
	    alt.Size('Adolescent fertility rate (births per 1,000 women ages 15-19):Q',scale=alt.Scale(range=[0,2000])),
	    alt.Color('CountryName:N'),
	    alt.OpacityValue(0.5),
	    alt.Shape('Country Code:N'),
	    alt.Tooltip('CountryName'),
	).properties(width=535, height=335).transform_filter(
		(alt.datum.Year>2010),
		)
	st.write(chart)
''' This chart is representing the fertility rate around the world for different countries in different years  '''
''' This kind of filters can be misleading because we filter some details and we let only things that we want to see , for example if we filter some years , and let only the present years visualized , it could miss leading about the data of some countries because we can not see the evaluation with time , so maybe something is missed about informations in the past and so we don't get the full image about what's going on '''
'''The next chart is the same as the previous one but without filtering , maybe the filter i applied is not realy deep in meaning , but we can use this kind of techniques to mislead the visualization and so mislead the reader ''' 
with st.echo():
	chart=alt.Chart(data).mark_circle(filled=True).encode(
	    alt.Y('Year',scale=alt.Scale(zero=False)),
	    alt.X('Fertility rate, total (births per woman):Q',scale=alt.Scale(zero=False)),
	    alt.Size('Adolescent fertility rate (births per 1,000 women ages 15-19):Q',scale=alt.Scale(range=[0,2000])),
	    alt.Color('CountryName:N'),
	    alt.OpacityValue(0.5),
	    alt.Shape('Country Code:N'),
	    alt.Tooltip('CountryName'),
	).properties(width=535, height=335)
	st.write(chart)
	
''' This is the chart with out any filters , we can see the difference between this and the  filtered one !, so filtering could be unethical in some way that we can hide lot of details that we don't like to be visualized'''
