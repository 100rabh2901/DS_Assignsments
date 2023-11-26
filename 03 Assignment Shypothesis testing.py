#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import numpy as np
from scipy import stats


# QUESTION 1-A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions.
# 
# 

# In[4]:


cutlets=pd.read_csv("Cutlets.csv")
cutlets


# In[5]:


'''
h0= unitA=unitB
h1= unitA!=unitB
we have to preform 2 sample 2 tail test
'''


# In[6]:


stats.ttest_ind(cutlets["Unit A"],cutlets["Unit B"])


# In[7]:


'''the value of p is greater than alpha
   so we go to the null hypothesis 
   there is no any significant difference in the diameter of the cutlet between two units.
'''


# QUESTION NO.2-A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch.
#    
#   Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.
# 

# In[8]:


labtat=pd.read_csv("LabTAT.csv")
labtat.head()


# H0= all the properties are equal
# H1= atleast one propertie is differeance
# 

# In[9]:


stats.f_oneway(labtat["Laboratory 1"],labtat["Laboratory 2"],labtat["Laboratory 3"],labtat["Laboratory 4"])[1]


# we see that the p value is greater than alpha 
# so we go for alternative hypothesis
# 

#  Sales of products in four different regions is tabulated for males and females. Find if male-female buyer rations are similar across regions!
#  

# In[ ]:





# In[22]:


buyer=pd.read_csv("BuyerRatio.csv")
buyer.head()


# In[ ]:


#H0=all the variable re equal.
#Ha=atlest one vriable is diffrent.


# In[25]:


table=buyer.iloc[:,1:6]
table


# In[26]:


stats.chi2_contingency(table)


# In[ ]:


#the p value is greater than alpha 0.05
#so we reject null hypothesis
#means, all the proporties are not equal


# Question-4 A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions.
# 

# In[ ]:


# hear h0 the defective percentage varies by center
#      ha the defective percentage does not varies by center


# In[30]:


cost=pd.read_csv("Costomer+OrderForm.csv")
cost.head()


# In[ ]:


# the data is in categorical form so we have to convert into tabular form.


# In[35]:


cost["Phillippines"].value_counts()


# In[36]:


cost["Indonesia"].value_counts()


# In[37]:


cost["Malta"].value_counts()


# In[39]:


cost["India"].value_counts()


# In[47]:


df={"Phillippnies":[271,29],
    "Indonesia":[267,33],
    "Malta":[269,31],
    "India":[280,20]
   }


# In[55]:


table=pd.DataFrame(df)


# In[56]:


table


# In[57]:


stats.chi2_contingency(table)


# In[58]:


#the pvalue is greater than alpha 0.05
#so we reject the null hyphothesis 
#means all the propertiesre not equal


# In[ ]:





# In[ ]:




