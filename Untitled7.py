#!/usr/bin/env python
# coding: utf-8

# In[150]:


import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
st.set_page_config(page_title="Inventory Analytics",page_icon=":random:",initial_sidebar_state='expanded')
st.title("INVENTORY AND SALES ANALYSIS OF SCMS")
df=pd.read_excel("C://Users//ajay//Downloads//COGS.xlsx")
df=df.drop([0])
x=df.columns
col1,col2=st.beta_columns(2)
with col1:
    item=st.selectbox("Select an Item",options=df[x[0]].values)
with col2:
    slct=st.selectbox("Select a Customised Metric",options=['Inventory','Ratio Analysis'])
for i in df[x[0]].values:
    if i in item:
        if 'Inventory' in slct:
            result=df.loc[df['Item']==i,[df.columns[j] for j in range(1,7) if j!=4]]
            st.table(result)
            chart_data = pd.DataFrame()
            chart_data['values'] = result.values.ravel()
            chart_data['labels'] = result.columns
            chart_v1 = alt.Chart(chart_data).mark_bar().encode(x='values',y='labels')
            st.write("", "", chart_v1)
        else:
            answer=df.loc[df['Item']==i,[df.columns[j] for j in range(4,11) if j!=5 if j!=6]]
            st.table(answer)


# In[ ]:





# In[ ]:





# In[ ]:




