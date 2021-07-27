#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Importing Data Set: Leading Cause of Death in NYC

# In[12]:


df = pd.read_csv(r"C:\Users\prati\Downloads\New_York_City_Leading_Causes_of_Death.csv")


# In[13]:


df


# ## EDA

# In[14]:


df.head()


# In[15]:


df.tail()


# In[16]:


df.info


# In[23]:


df.isnull()


# ## Dropping Unwanted Columns

# In[17]:


df.drop("Age Adjusted Death Rate", axis=1, inplace = True)


# In[18]:


df


# ### Renaming Columns 

# In[19]:


df.rename(columns={'Leading Cause': 'Cause of Death', 'Sex': 'Gender'}, inplace = True)


# In[20]:


df


# In[27]:


df.groupby(['Year'])['Deaths'].count()


# ### Examining Deaths over the years 

# In[32]:


df.groupby(['Year'])['Deaths'].count().plot(kind='bar')


# In[37]:


df.groupby(['Cause of Death'])['Deaths'].count()


# In[38]:


df.groupby(['Cause of Death'])['Deaths'].count().plot(kind='bar')


# In[39]:


df.groupby(['Cause of Death'])['Deaths'].max()


# In[41]:


df.groupby(['Gender'])['Deaths'].count()


# ### Replacing "F" and "M" in the Dataset with "Female" and "Male" 

# In[54]:


df['Gender'][df['Gender'] == 'F'] = 'Female'


# In[55]:


df


# In[56]:


df['Gender'][df['Gender'] == 'M'] = 'Male'


# In[59]:


df


# ### Deaths by Gender 

# In[60]:


df.groupby(['Gender'])['Deaths'].count()


# In[106]:


df.groupby(['Gender'])['Deaths'].count().plot(kind='bar')


# In[66]:


df['Death Rate'].dtype


# In[75]:


df['Death Rate'] = pd.to_numeric


# In[69]:


print(df.dtypes)


# In[71]:


df


# In[87]:


df['Deaths']=pd.to_numeric


# In[88]:


df['Deaths'].dtpye


# ### Death by Race Ethnicity 

# In[94]:


df.groupby(['Race Ethnicity'])['Deaths'].count()


# In[99]:


df.groupby(['Race Ethnicity'])['Deaths'].count().plot(kind='bar')


# In[101]:


df.plot(kind='hist')


# In[103]:


df.plot(kind='scatter', x='Race Ethnicity', y='Cause of Death')


# In[ ]:




