#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


input_file = "customer_input.txt"
output_file = "customer_output.csv"


# In[2]:


df = pd.read_csv(input_file, sep=",")


# In[4]:


df["timestamp"] = pd.to_datetime(df["timestamp"])
print(df["timestamp"])


# In[7]:


df["date"] = df["timestamp"].dt.date
print(df["date"])


# In[8]:



df["total_spent"] = df["product_price"] * df["quantity"]
print(df["total_spent"])


# In[9]:


grouped = df.groupby(["date", "customer_id"])["total_spent"].sum().reset_index()
print(grouped)


# In[ ]:


grouped.to_csv(output_file, index=False)


# In[ ]:





# In[ ]:





# In[ ]:




