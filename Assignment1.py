#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


input_file = r'C:\Users\sarin\Documents\Untitled Folder\uservisited.csv'
output_file = "user_visited_output.csv"

df = pd.read_csv(input_file)

print(df)


# In[11]:



total_interactions = len(df)
print(total_interactions)


# In[12]:


total_unique_users = len(df["user_id"].unique())
print(total_unique_users)


# In[22]:


print(df['url'][30])


# In[14]:


most_visited_url = df["url"].value_counts().index[0]
print(df["url"].value_counts())
print(most_visited_url)


# In[16]:


average_time_spent = df.groupby("url")["page_view_duration"].mean()
print(average_time_spent)


# In[10]:


with open(output_file, "w") as f:
    f.write("Total Interactions,Total Unique Users,Most Visited URL,Average Time Spent on Each URL\n")
    f.write(f"{total_interactions},{total_unique_users},{most_visited_url},{average_time_spent.mean()}\n")


# In[ ]:




