#!/usr/bin/env python
# coding: utf-8

# In[86]:


pip install tabulate


# In[64]:


import mysql.connector as c


# In[65]:


import pandas as pd


# In[73]:


connection = c.connect(host= "localhost",user= "root", database = "multi_spe_hospital")


# In[74]:


cursor = connection.cursor()


# In[75]:


query2 = "select * from patients"


# In[76]:


# executing cursor
cursor.execute(query2)


# In[77]:


# fetching tables
table_rows = cursor.fetchall()
print("Total Number of rows in table:", cursor.rowcount)


# In[78]:


df


# In[81]:


def show_data(country):
    data = df.loc[df['COUNTRY'] == country]
    print(data)


# In[87]:


def get_file(country):
    data = df.loc[df['COUNTRY'] == country]
    file_name = str(country)
    data.to_csv('C:/Users/prate/Table_' + country + ".csv")  # replace path with your desired path
    print("File has been created to the specified path")


# In[88]:


# calling functions

df1= show_data("IND")
get_file("IND")


# In[92]:


# displaying the DataFrame in table
from tabulate import tabulate
print(tabulate(df1, headers = 'keys', tablefmt = 'sql'))


# In[93]:


show_data("AUS")
get_file("AUS")


# In[ ]:




