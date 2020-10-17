#!/usr/bin/env python
# coding: utf-8

# ## TASK-4
# ## B.CHANDRA SAGAR

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:



data=pd.read_csv('D:\\SampleSuperstore.csv')


# In[3]:


data.head(10)


# In[4]:


print('DIMENSIONS {} \n'.format(data.shape))
print('COLUMNS {} \n'.format(data.columns))
print('Null items {} \n'.format(data.isnull().sum()))
print('Duplicates {} \n'.format(data.duplicated().sum()))
print(data.describe(),'\n')
data.info()


# In[5]:


print('Shipped to countries {}\n'.format(data['Country'].unique()))
print('states {}\n'.format(data['State'].unique()))
print('category {}\n'.format(data['Category'].unique()))
print('Sub-category {}\n'.format(data['Sub-Category'].unique()))
print('segment {}\n'.format(data['Segment'].unique()))
print('Regions {}\n'.format(data['Region'].unique()))


# In[6]:


#removing duplicates
data=data.drop_duplicates()
print('duplicates {}'.format(data.duplicated().sum()))


# In[7]:


plt.figure()
sns.pairplot(data)


# In[9]:


#sales and profit of different segments 


# In[8]:


inf1=data.groupby('Category').sum()[['Sales','Quantity','Profit']]


# In[9]:



plt.figure(figsize=(15,7))
plt.bar([1,2,3],inf1['Sales'],width=0.3,label='Sales')
plt.bar([1.3,2.3,3.3],inf1['Quantity'],width=0.3,color='green',label='Quantity')
plt.bar([1.6,2.6,3.6],inf1['Profit'],width=0.3,color='orange',label='Profit')
plt.gca().set_xticks([1,2,3])
plt.gca().set_xticklabels(['Furniture','Office supplies','Technology'])
plt.legend()


# ## Technology category has the highest sales and profit even though the quantity sold is less than the other two categories 

# In[10]:


inf2=data.groupby('Segment').sum()[['Sales','Quantity','Profit']]


# In[11]:


plt.bar(['Consumer','Corporate','Home office'],inf2['Sales'],width=0.6)
plt.ylabel('SALES')
plt.figure()
plt.bar(['Consumer','Corporate','Home office'],inf2['Quantity'],width=0.6,color='green')
plt.ylabel('Quantity')
plt.figure()
plt.bar(['Consumer','Corporate','Home office'],inf2['Profit'],width=0.6,color='orange')
plt.ylabel('Profit')


# ## From the above graph we can infer that sales and profit in the consumer category are the highest and home office are the least

# In[12]:


#sales in different states
inf3=data.groupby('State').sum()[['Sales','Quantity','Profit']]
plt.figure(figsize=(15,10))
plt.bar(inf3.index,inf3['Sales'])
plt.xticks(rotation=90);
plt.ylabel('SALES');


# 

# In[68]:


#profits in different states
plt.figure(figsize=(15,10))
plt.bar(inf3.index,inf3['Profit'])
plt.xticks(rotation=90);
plt.ylabel('PROFIT');


# ## Sales in texas are among the top three but has the lowest profit of all states (negative)

# In[122]:


#shipping mode
inf4=data.groupby('Ship Mode').count()['Quantity']
plt.bar(inf4.index,inf4,color='red')
plt.ylabel('count');


# In[33]:


ins=data.groupby('Ship Mode').sum()
plt.pie(ins['Profit'],labels=ins.index,autopct="%1.1f%%");
plt.title('PROFIT DISTRIBUTION');


# ## Most preferred shipping mode is standard class and least preferred is same day
# ## Standard class shipping mode has the highest profits followed by second class,first class and same day 

# In[121]:


#region
inf5=data.groupby('Region').sum()[['Sales','Quantity','Profit']]
inf5
fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(15,5))
ax1.bar(inf5.index,inf5['Sales'],color=['green','blue','yellow','red'])
ax1.set_ylabel('Sales')
ax2.bar(inf5.index,inf5['Quantity'],color=['green','blue','yellow','red'])
ax2.tick_params(right=True,left=False,labelleft=False,labelright=True)
ax2.set_ylabel('Quantity')
ax3.bar(inf5.index,inf5['Profit'],color=['green','blue','yellow','red'])
ax3.tick_params(right=True,left=False,labelleft=False,labelright=True)
ax3.set_ylabel('Profit');


# ## sales,quantity and profit distribution of different regions

# In[177]:


fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(18,18))
ax1.pie(data.groupby('Category').count()['Quantity'],labels=data.groupby('Category').count()['Quantity'].index,autopct='%1.1f%%');
ax1.set_title('COUNT')
#plt.figure()
ax2.pie(data.groupby('Category').sum()['Sales'],labels=data.groupby('Category').sum()['Sales'].index,autopct='%1.1f%%');
ax2.set_title('SALES')
#ax2.figure()
ax3.pie(data.groupby('Category').sum()['Profit'],labels=data.groupby('Category').sum()['Profit'].index,autopct='%1.1f%%');
ax3.set_title('PROFIT');


# ## 1.Office supplies is the most frequently shipped category
# ## 2.The sales  percentage of all three categories is almost same
# ## 3.Eventough the sales of all three categories are almost same, technology and office supplies hold maximum profit whereas furniture has very low profit percentage considering the fact that it has higher sales and quantity than technology

# In[163]:


inf6=data.groupby('Sub-Category').sum()
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(15,10)) 
ax1.bar(inf6.index,inf6['Quantity'],color='orange')
ax1.tick_params(axis='x',labelrotation=90)
ax1.set_ylabel('Quantity')
ax2.bar(inf6.index,inf6['Profit'],color='orange')
ax2.tick_params(axis='x',labelrotation=90)
ax2.set_ylabel('Profit')


# ## From the above graphs we can infer that blinders have high demand but highest profits come from copiers even though the quantity of copiers sold is the least among all so increasing sales of copiers may lead to more profit

# In[25]:


#Discounts vs profits
sns.lineplot(data['Discount'],data['Profit'])


# In[ ]:




