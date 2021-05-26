#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
st.set_page_config(page_title="Netscore Inventory Analytics",page_icon=":random:",initial_sidebar_state='expanded')
st.title("LIST OF ITEMS INVENTORY")
df=pd.read_csv("https://raw.githubusercontent.com/Ajaybabuds/Work/main/month_inv.csv",sep=',')
df=df.iloc[:,1:]
x=df.columns
df['year']=df['year'].astype('str')
y=['2019','2020','2021']
col1,col2,col3=st.beta_columns(3)
with col1:
    yr=st.selectbox("Select Year:",options=['2019','2020','2021'])
    
with col2:
    item=st.selectbox("Select an Item:",options=df[x[0]].value_counts().index)
with col3:
    slct=st.selectbox("Select a Customized Metric:",options=['Inventory','Ratio Analysis'])
for j in y:
    if j in yr:
        for i in df[x[0]].value_counts().index:
            if i in item:
                if 'Inventory' in slct:
                    res=pd.DataFrame(df.loc[(df['year']==j) & (df['Item']==i)].groupby(['month']).sum()).drop(['Cost'],axis=1)
                    res['End_inv']=res['Aftr_adj_Qty']-res['Sales_Qty']
                    res['Cum_End_inv']=res['End_inv'].cumsum()
                    st.table(res)
                else:
                    res=pd.DataFrame(df.loc[(df['year']==j) & (df['Item']==i)].groupby(['month']).sum())
                    res['End_inv']=res['Aftr_adj_Qty']-res['Sales_Qty']
                    res['COGS']=res['Cost']-((res['Cost']/res['Aftr_adj_Qty'])*res['End_inv'])
                    res['avg_inv']=(res['End_inv']+res['End_inv'].shift(1))/2
                    res['inv_turnover']=res['COGS']/res['avg_inv']
                    res['DSI']=365/res['inv_turnover']
                    res2=res.iloc[:,6:]
                    st.table(res2)
                 


# In[ ]:





# In[ ]:





# In[ ]:




