#!/usr/bin/env python
# coding: utf-8

# In[2]:


import warnings
warnings.filterwarnings('ignore')
import streamlit as st
st.title("TYRE PURCHASES OF A CLIENT")
st.header("Total Sales by Different Categories")
import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\ajay\\Downloads\\Sales Data.csv")
df=df.drop_duplicates(subset=['Internal ID'])
sts=df.groupby(['Status']).sum().drop(['Internal ID','Item Rate','Quantity'],axis=1).round(2)
df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].apply(lambda x:x.strftime('%B'))
df['Year']=df['Date'].dt.year
yr=df.groupby(['Year']).sum().drop(['Internal ID','Item Rate','Quantity'],axis=1)
mnth=df.groupby(['Month']).sum().drop(['Internal ID','Item Rate','Quantity','Year'],axis=1)
df1=df.groupby(['Year','Month']).sum().drop(['Internal ID','Item Rate','Quantity'],axis=1).unstack().fillna(0)
number=st.number_input("Insert a number",2014,2021)
st.write(number)
color=st.selectbox('Select a Sales by',options=['Status','Year','Month'])
if 'Status' in color:
        st.table(sts)
        st.bar_chart(sts)
elif 'Year' in color:
        y=st.selectbox("Select below year",options=[2014,2015,2016,2017,2018,2019,2020,2021])
        h=[2014,2015,2016,2017,2018,2019,2020,2021]
        if number in h:
            x=df1.loc[number,:]
            st.table(x)
elif 'Month' in color:
        m=st.select_slider("Select Month",options=['April','May','June','July','August','September','October','November','December',
                                                  'January','February','March'])
        j=['April','May','June','July','August','September','October','November','December',
                                                  'January','February','March']
        for i in j:
            if i in m:
                st.write("Sales by Month:",mnth.loc[i,:])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




